"""Token."""

from base64 import b64encode
from typing import Tuple

import requests

from ..models.token import TokenResponseSchema


class Token:
    """Token."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def generate_token(
        self,
        username: str,
        password: str,
    ) -> Tuple[str, TokenResponseSchema | None]:
        """Use your account as HTTPBasic Auth to generate your token to use the API.
        You can also generate your token directly on the website."""
        try:
            basic = b64encode(f"{username}:{password}".encode("UTF-8")).decode("UTF-8")
            print("Basic:", basic)

            response = requests.post(
                url=f"{self.api_url}/token",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": f"Basic {basic}",
                },
            )

            response.raise_for_status()

            return (
                "Token generated successfully",
                TokenResponseSchema.model_validate(response.json()),
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 422:
                    return (
                        "Request could not be processed due to an invalid payload.",
                        None,
                    )
                case 455:
                    return "Failed to generate token.", None
                case _:
                    return f"Unknown error: {error}", None
