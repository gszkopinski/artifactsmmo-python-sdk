"""Accounts."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.accounts import AccountsResponseSchema


class Accounts:
    """Accounts."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def create_account(
        self,
        username: Annotated[
            str,
            Field(
                description="Your desired username.",
                pattern="^[a-zA-Z0-9_-]+$",
                ge=6,
                le=32,
            ),
        ],
        password: Annotated[
            str,
            Field(
                description="Your password.",
                min_length=5,
                max_length=50,
            ),
        ],
        email: Annotated[
            str,
            Field(
                description="Your email.",
                format="email",
            ),
        ],
    ) -> Tuple[str, AccountsResponseSchema | None]:
        """Create new account."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/accounts/create",
                json={
                    "username": username,
                    "password": password,
                    "email": email,
                },
            )

            response.raise_for_status()

            return (
                "Account created successfully.",
                AccountsResponseSchema.model_validate(response.json()),
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 422:
                    return (
                        "Request could not be processed due to an invalid payload.",
                        None,
                    )
                case 456:
                    return "This username is already taken.", None
                case 457:
                    return "This email is already in use.", None
                case _:
                    return f"Unknown error: {error}", None
