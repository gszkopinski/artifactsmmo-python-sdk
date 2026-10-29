"""Characters."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.characters import (
    CharacterResponseSchema,
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
            ),
        ],
        skin: Annotated[str, Field(description="Your desired skin.")],
    ) -> tuple[str, CharacterResponseSchema | None]:
        """Create new character on your account. You can create up to 5 characters."""
        return self._request(
            "POST",
            "/characters/create",
            CharacterResponseSchema,
            "Successfully created character.",
            {
                404: "Skin not found.",
                494: "This name is already in use.",
                495: "You have reached the maximum number of characters on your account.",
                550: "You cannot choose this skin because you do not own it.",
            },
            json={
                "name": name,
                "skin": skin,
            },
        )

    def delete_character(
        self,
        name: Annotated[
            str, Field(description="Character name.", pattern="^[a-zA-Z0-9_-]+$")
        ],
    ) -> tuple[str, CharacterResponseSchema | None]:
        """Delete character on your account."""
        return self._request(
            "POST",
            "/characters/delete",
            CharacterResponseSchema,
            "Successfully deleted character.",
            json={
                "name": name,
            },
        )
