"""Npcs."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.npcs import (
    NPCType,
    StaticDataPage_NPCSchema_,
)


class Npcs(BaseModule):
    """Npcs."""

    def get_all_npcs(
        self,
        name: Annotated[
            str | None,
            Field(
                description="NPC name.",
                pattern="^[a-zA-Z0-9_-]+(\\s[a-zA-Z0-9_-]+)*\\s?$",
            ),
        ] = None,
        type: Annotated[NPCType | None, Field(description="Type of NPCs.")] = None,
        currency: Annotated[
            str | None,
            Field(
                description="Currency code to filter NPCs that trade with this currency.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        item: Annotated[
            str | None,
            Field(
                description="Item code to filter NPCs that trade this item.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_NPCSchema_ | None]:
        """Fetch NPCs details."""
        return self._request(
            "GET",
            "/npcs/details",
            StaticDataPage_NPCSchema_,
            "Successfully fetched NPCs.",
            params={
                "name": name,
                "type": type,
                "currency": currency,
                "item": item,
                "page": page,
                "size": size,
            },
        )
