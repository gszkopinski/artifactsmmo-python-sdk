"""Monsters."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.monsters import (
    MonsterResponseSchema,
    StaticDataPage_MonsterSchema_,
)


class Monsters(BaseModule):
    """Monsters."""

    def get_all_monsters(
        self,
        name: Annotated[
            str | None,
            Field(
                description="Name of the monster.",
                pattern="^[a-zA-Z0-9_-]+(\\s[a-zA-Z0-9_-]+)*\\s?$",
            ),
        ] = None,
        min_level: Annotated[
            int | None, Field(description="Minimum level.", ge=0)
        ] = None,
        max_level: Annotated[
            int | None, Field(description="Maximum level.", ge=0)
        ] = None,
        drop: Annotated[
            str | None,
            Field(description="Item code of the drop.", pattern="^[a-zA-Z0-9_-]+$"),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_MonsterSchema_ | None]:
        """Fetch monsters details."""
        return self._request(
            "GET",
            "/monsters",
            StaticDataPage_MonsterSchema_,
            "Successfully fetched monsters.",
            params={
                "name": name,
                "min_level": min_level,
                "max_level": max_level,
                "drop": drop,
                "page": page,
                "size": size,
            },
        )

    def get_monster(
        self,
        code: Annotated[
            str,
            Field(description="The code of the monster.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, MonsterResponseSchema | None]:
        """Retrieve the details of a monster."""
        return self._request(
            "GET",
            f"/monsters/{code}",
            MonsterResponseSchema,
            "Successfully fetched monster.",
            {
                404: "monster not found.",
            },
        )
