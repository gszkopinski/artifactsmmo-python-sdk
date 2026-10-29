"""Accounts."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.accounts import (
    AccountAchievementSchemaPage,
    CharactersListSchema,
)
from ..models.common import (
    AchievementType,
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
