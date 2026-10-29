"""Accounts."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.accounts import AccountsResponseSchema


class Accounts(BaseModule):
    """Accounts."""

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
    ) -> tuple[str, AccountsResponseSchema | None]:
        """Create new account."""
        return self._request(
            "POST",
            "/accounts/create",
            AccountsResponseSchema,
            "Account created successfully.",
            {
                456: "This username is already taken.",
                457: "This email is already in use.",
            },
            json={
                "username": username,
                "password": password,
                "email": email,
            },
        )
