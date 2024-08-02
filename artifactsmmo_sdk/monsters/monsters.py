"""Monsters."""

import requests

from ..models.monsters import MonsterResponseSchema


class Monsters:
    """Monsters."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def get_monster(self, code: str) -> MonsterResponseSchema:
        """Retrieve the details of a monster."""
        response = self.session.get(
            url=f"{self.api_url}/monsters/{code}",
        )

        response.raise_for_status()

        return MonsterResponseSchema.model_validate(response.json())
