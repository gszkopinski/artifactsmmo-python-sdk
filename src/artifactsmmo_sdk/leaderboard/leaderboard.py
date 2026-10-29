"""Leaderboard."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.leaderboard import (
    CharacterLeaderboardSchemaPage,
    CharacterLeaderboardType,
)


class Leaderboard(BaseModule):
    """Leaderboard."""

    def get_characters_leaderboard(
        self,
        sort: Annotated[
            CharacterLeaderboardType | None,
            Field(description="Sort of character leaderboards."),
        ] = None,
        name: Annotated[
            str | None,
            Field(
                description="Character name.",
                pattern="^[a-zA-Z0-9_-]+(\\s[a-zA-Z0-9_-]+)*\\s?$",
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, CharacterLeaderboardSchemaPage | None]:
        """Fetch leaderboard details."""
        return self._request(
            "GET",
            "/leaderboard/characters",
            CharacterLeaderboardSchemaPage,
            "Successfully fetched leaderboard.",
            params={
                "sort": sort,
                "name": name,
                "page": page,
                "size": size,
            },
        )
