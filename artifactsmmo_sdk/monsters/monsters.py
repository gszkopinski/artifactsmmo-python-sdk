"""Monsters."""

import requests

from ..models.monsters import MonsterResponseSchema, ListMonsterResponseSchema


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

    def get_all_monsters(
        self,
        drop: str,
        max_level: int,
        min_level: int,
        page: int = 1,
        size: int = 50,
    ) -> ListMonsterResponseSchema:
        """Return monsters."""
        parameters = f"drop={drop}"
        parameters += f"&max_level={max_level}"
        parameters += f"&min_level={min_level}"
        parameters += f"&page={page}"
        parameters += f"&size={size}"

        response = self.session.get(
            url=f"{self.api_url}/monsters?{parameters}",
        )

        response.raise_for_status()

        return ListMonsterResponseSchema.model_validate(response.json())