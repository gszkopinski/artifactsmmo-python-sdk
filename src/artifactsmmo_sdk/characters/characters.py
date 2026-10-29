"""Characters."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.characters import (
    CharacterResponseSchema,
    CharacterSkinEnum,
    CharacterSortEnum,
    ListCharacterResponseSchema,
)


class Characters(BaseModule):
    """Characters."""

    def create_character(
        self,
        name: Annotated[
            str,
            Field(
                description="Your desired character name. It's unique and all players can see it.",
                pattern="^[a-zA-Z0-9_-]+$",
                min_length=3,
                max_length=12,
            ),
        ],
        skin: Annotated[CharacterSkinEnum, Field(description="Your desired skin.")],
    ) -> tuple[str, CharacterResponseSchema | None]:
        """Create new character on your account. You can create up to 5 characters."""
        return self._request(
            "POST",
            "/characters/create",
            CharacterResponseSchema,
            "Successfully created character.",
            {
                494: "Name already used.",
                495: "Maximum characters reached on your account.",
            },
            json={"name": name, "skin": skin},
        )

    def delete_character(
        self,
        name: Annotated[
            str,
            Field(
                description="Character name.",
                pattern="^[a-zA-Z0-9_-]+$",
                min_length=3,
                max_length=12,
            ),
        ],
    ) -> tuple[str, CharacterResponseSchema | None]:
        """Delete character on your account."""
        return self._request(
            "POST",
            "/characters/delete",
            CharacterResponseSchema,
            "Successfully deleted character.",
            json={"name": name},
        )

    def get_all_characters(
        self,
        sort: Annotated[
            str,
            Field(
                description="Default sort by combat total XP.",
                default="xp",
            ),
        ] = CharacterSortEnum.GOLD.value,
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, ListCharacterResponseSchema | None]:
        """Fetch characters details."""
        return self._request(
            "GET",
            "/characters",
            ListCharacterResponseSchema,
            "Successfully fetched characters details.",
            {
                404: "Characters not found.",
            },
            params={
                "sort": sort,
                "page": page,
                "size": size,
            },
        )

    def get_character(
        self,
        name: str,
    ) -> tuple[str, CharacterResponseSchema | None]:
        """Retrieve the details of a character."""
        return self._request(
            "GET",
            f"/characters/{name}",
            CharacterResponseSchema,
            "Successfully fetched character.",
            {
                404: "Character not found.",
            },
        )
