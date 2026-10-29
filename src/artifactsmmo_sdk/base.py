"""Shared plumbing for the API modules."""

from enum import Enum
from typing import Any, TypeVar

import requests
from pydantic import BaseModel
from requests import PreparedRequest
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

DEFAULT_TIMEOUT = 30

SchemaT = TypeVar("SchemaT", bound=BaseModel)

# Messages of the API spec shared by most endpoints. Endpoint specific codes are passed to
# `_request(errors=...)` and take precedence over these.
COMMON_ERRORS: dict[int, str] = {
    422: "Request could not be processed due to an invalid payload.",
    478: "Missing required item(s).",
    486: "An action is already in progress for this character.",
    497: "The character's inventory is full.",
    498: "Character not found.",
    499: "The character is in cooldown.",
}


class SessionAdapter(HTTPAdapter):
    """Adapter applying a default timeout and a retry on HTTP 429 only.

    Only 429 is retried: the API did not execute the request in that case, so
    it is safe even for POST actions.
    """

    def __init__(self, timeout: float = DEFAULT_TIMEOUT) -> None:
        """Init."""
        self.timeout = timeout
        super().__init__(
            max_retries=Retry(
                total=3,
                status_forcelist=[429],
                allowed_methods=None,
                backoff_factor=1,
                respect_retry_after_header=True,
                raise_on_status=False,
            ),
        )

    def send(self, request: PreparedRequest, **kwargs: Any) -> requests.Response:  # type: ignore[override]
        """Send with the default timeout if none was given."""
        if kwargs.get("timeout") is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


def build_session(token: str) -> requests.Session:
    """Create the authenticated session shared by all modules."""
    session = requests.Session()
    session.headers.update(
        {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
    )
    adapter = SessionAdapter()
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


class BaseModule:
    """Base class of the API modules."""

    def __init__(self, api_url: str, session: requests.Session) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def _request(
        self,
        method: str,
        path: str,
        schema: type[SchemaT],
        success: str,
        errors: dict[int, str] | None = None,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | list[Any] | None = None,
        common_errors: bool = True,
    ) -> tuple[str, SchemaT | None]:
        """Call the API and return `(message, data)`.

        `data` is None when the call failed. Status codes found in `errors`
        (then in COMMON_ERRORS) give their message, others give a generic one.
        None values in `params` and in a dict `json` are dropped.
        """
        try:
            response = self.session.request(
                method,
                f"{self.api_url}{path}",
                params={
                    k: v.value if isinstance(v, Enum) else v
                    for k, v in (params or {}).items()
                    if v is not None
                },
                json=(
                    {k: v for k, v in json.items() if v is not None}
                    if isinstance(json, dict)
                    else json
                ),
            )
            response.raise_for_status()
            return success, schema.model_validate(response.json())
        except requests.exceptions.HTTPError as error:
            known = {**(COMMON_ERRORS if common_errors else {}), **(errors or {})}
            status = error.response.status_code
            return known.get(status, f"Unknown error: {error}"), None
