"""Monsters."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.monsters import ListMonsterResponseSchema, MonsterResponseSchema


class Monsters(BaseModule):
    """Monsters."""

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
                404: "Monster not found.",
            },
        )

    def get_all_monsters(
        self,
        drop: Annotated[
            str, Field(description="Item code of the drop.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        max_level: Annotated[int, Field(description="Monster maximum level.", ge=0)],
        min_level: Annotated[int, Field(description="Monster minimum level.", ge=0)],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, ListMonsterResponseSchema | None]:
        """Fetch monsters details."""
        return self._request(
            "GET",
            "/monsters",
            ListMonsterResponseSchema,
            "Successfully fetched monsters details.",
            {
                404: "Monsters not found.",
            },
            params={
                "page": page,
                "size": size,
                "drop": drop or None,
                "max_level": max_level or None,
                "min_level": min_level or None,
            },
        )
