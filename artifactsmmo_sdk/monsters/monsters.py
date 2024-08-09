"""Monsters."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.monsters import ListMonsterResponseSchema, MonsterResponseSchema


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

    def get_monster(
        self,
        code: Annotated[str, Field(description="The code of the monster.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, MonsterResponseSchema | None]:
        """Retrieve the details of a monster."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/monsters/{code}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched monster.",
                MonsterResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Monster not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_all_monsters(
        self,
        drop: Annotated[str, Field(description="Item code of the drop.", pattern="^[a-zA-Z0-9_-]+$")],
        max_level: Annotated[int, Field(description="Monster maximum level.", ge=0)],
        min_level: Annotated[int, Field(description="Monster minimum level.", ge=0)],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[int, Field(description="Page size.", ge=1, le=100, default=50)] = 50,
    ) -> Tuple[str, ListMonsterResponseSchema | None]:
        """Fetch monsters details."""
        try:
            parameters = f"drop={drop}"
            parameters += f"&max_level={max_level}"
            parameters += f"&min_level={min_level}"
            parameters += f"&page={page}"
            parameters += f"&size={size}"

            response = self.session.get(
                url=f"{self.api_url}/monsters?{parameters}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched monsters details.",
                ListMonsterResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Monsters not found.", None
                case _:
                    return f"Unknown error: {error}", None
