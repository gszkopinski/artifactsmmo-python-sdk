"""Characters."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.characters import (
    CharacterResponseSchema,
    CharacterSkinEnum,
    CharacterSortEnum,
    ListCharacterResponseSchema,
)


class Characters:
    """Characters."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def create_character(
        self,
        name: Annotated[str, Field(
            description="Your desired character name. It's unique and all players can see it.",
            pattern="^[a-zA-Z0-9_-]+$",
            min_length=3,
            max_length=12,
        )],
        skin: Annotated[CharacterSkinEnum, Field(description="Your desired skin.")],
    ) -> Tuple[str, CharacterResponseSchema | None]:
        """Create new character on your account. You can create up to 5 characters."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/characters/create",
                json={"name": name, "skin": skin},
            )

            response.raise_for_status()

            return (
                "Successfully created character.",
                CharacterResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 494:
                    return "Name already used.", None
                case 495:
                    return "Maximum characters reached on your account.", None
                case _:
                    return f"Unknown error: {error}", None

    def delete_character(
        self,
        name: Annotated[str, Field(
            description="Character name.",
            pattern="^[a-zA-Z0-9_-]+$",
            min_length=3,
            max_length=12,
        )],
    ) -> Tuple[str, CharacterResponseSchema | None]:
        """Delete character on your account."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/characters/delete",
                json={"name": name},
            )

            response.raise_for_status()

            return (
                "Successfully deleted character.",
                CharacterResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 498:
                    return "Character not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_all_characters(
        self,
        sort: Annotated[str, Field(
            description="Default sort by combat total XP.",
            default="xp",
        )] = CharacterSortEnum.GOLD.value,
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[int, Field(description="Page size.", ge=1, le=100, default=50)] = 50,
    ) -> Tuple[str, ListCharacterResponseSchema | None]:
        """Fetch characters details."""
        try:
            parameters = f"sort={sort}"
            parameters += f"&page={page}"
            parameters += f"&size={size}"

            response = self.session.get(
                url=f"{self.api_url}/characters?{parameters}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched characters details.",
                ListCharacterResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Characters not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_character(
        self,
        name: str,
    ) -> Tuple[str, CharacterResponseSchema | None]:
        """Retrieve the details of a character."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/characters/{name}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched character.",
                CharacterResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Character not found.", None
                case _:
                    return f"Unknown error: {error}", None
