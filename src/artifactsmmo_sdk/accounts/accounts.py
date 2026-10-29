"""Accounts."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.accounts import (
    AccountAchievementSchemaPage,
    CharactersListSchema,
    PasswordResetResponseSchema,
)
from ..models.common import (
    AchievementType,
    ResponseSchema,
)


class Accounts(BaseModule):
    """Accounts."""

    def get_account_achievements(
        self,
        account: Annotated[
            str,
            Field(description="The name of the account.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        type: Annotated[
            AchievementType | None, Field(description="Type of achievements.")
        ] = None,
        completed: Annotated[
            bool | None, Field(description="Filter by completed achievements.")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, AccountAchievementSchemaPage | None]:
        """Retrieve the achievements of a account."""
        return self._request(
            "GET",
            f"/accounts/{account}/achievements",
            AccountAchievementSchemaPage,
            "Successfully fetched achievements.",
            {
                404: "Account not found.",
            },
            params={
                "type": type,
                "completed": completed,
                "page": page,
                "size": size,
            },
        )

    def get_account_characters(
        self,
        account: Annotated[
            str,
            Field(description="The name of the account.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, CharactersListSchema | None]:
        """Account character lists."""
        return self._request(
            "GET",
            f"/accounts/{account}/characters",
            CharactersListSchema,
            "Successfully fetched account characters.",
        )

    def create_account(
        self,
        username: Annotated[
            str, Field(description="Your desired username.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        password: Annotated[
            str, Field(description="Your password.", pattern="^[^\\s]+$")
        ],
        email: Annotated[str, Field(description="Your email.")],
    ) -> tuple[str, ResponseSchema | None]:
        """Create Account"""
        return self._request(
            "POST",
            "/accounts/create",
            ResponseSchema,
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

    def forgot_password(
        self,
        email: Annotated[str, Field(description="Your email address.")],
    ) -> tuple[str, PasswordResetResponseSchema | None]:
        """Request a password reset."""
        return self._request(
            "POST",
            "/accounts/forgot_password",
            PasswordResetResponseSchema,
            "If this email address is associated with an account, a reset link has been sent.",
            json={
                "email": email,
            },
        )

    def reset_password(
        self,
        token: Annotated[str, Field(description="Password reset token.")],
        new_password: Annotated[
            str, Field(description="Your new password.", pattern="^[^\\s]+$")
        ],
    ) -> tuple[str, PasswordResetResponseSchema | None]:
        """Reset password with a token. Use /forgot_password to get a token by email."""
        return self._request(
            "POST",
            "/accounts/reset_password",
            PasswordResetResponseSchema,
            "Password has been successfully reset.",
            {
                560: "The password reset token is invalid.",
                561: "The password reset token has expired.",
                562: "This password reset token has already been used.",
            },
            json={
                "token": token,
                "new_password": new_password,
            },
        )
