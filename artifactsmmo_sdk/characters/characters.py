"""Characters."""

import requests

from ..models.characters import CharacterResponseSchema, CharacterSkinEnum


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

    def get_character(
        self,
        name: str,
    ) -> CharacterResponseSchema:
        """Get character from his name."""
        response = self.session.get(
            url=f"{self.api_url}/characters/{name}",
        )

        response.raise_for_status()

        return CharacterResponseSchema.model_validate(response.json())

    def create_character(
        self,
        name: str,
        skin: CharacterSkinEnum,
    ) -> CharacterResponseSchema:
        """Create a character."""
        response = self.session.post(
            url=f"{self.api_url}/characters/create",
            body={"name": name, "skin": skin},
        )

        response.raise_for_status()

        return CharacterResponseSchema.model_validate(response.json())
