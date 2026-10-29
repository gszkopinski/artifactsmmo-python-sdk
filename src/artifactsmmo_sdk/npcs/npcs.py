"""Npcs."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.npcs import (
    NPCResponseSchema,
    NPCType,
    StaticDataPage_NPCItemSchema_,
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

    def get_npc(
        self,
        code: Annotated[
            str, Field(description="The code of the NPC.", pattern="^[a-zA-Z0-9_-]+$")
        ],
    ) -> tuple[str, NPCResponseSchema | None]:
        """Retrieve the details of a NPC."""
        return self._request(
            "GET",
            f"/npcs/details/{code}",
            NPCResponseSchema,
            "Successfully fetched NPC.",
            {
                404: "NPC not found.",
            },
        )

    def get_npc_items(
        self,
        code: Annotated[
            str, Field(description="The code of the NPC.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_NPCItemSchema_ | None]:
        """Retrieve the items list of a NPC. If the NPC has items to buy, sell or trade, they will be displayed."""
        return self._request(
            "GET",
            f"/npcs/items/{code}",
            StaticDataPage_NPCItemSchema_,
            "Successfully fetched NPC items.",
            {
                404: "NPC items not found.",
            },
            params={
                "page": page,
                "size": size,
            },
        )

    def get_all_npcs_items(
        self,
        code: Annotated[
            str | None, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ] = None,
        npc: Annotated[
            str | None, Field(description="NPC code.", pattern="^[a-zA-Z0-9_-]+$")
        ] = None,
        currency: Annotated[
            str | None, Field(description="Currency code.", pattern="^[a-zA-Z0-9_-]+$")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_NPCItemSchema_ | None]:
        """Retrieve the list of all NPC items."""
        return self._request(
            "GET",
            "/npcs/items",
            StaticDataPage_NPCItemSchema_,
            "Successfully fetched NPC items.",
            params={
                "code": code,
                "npc": npc,
                "currency": currency,
                "page": page,
                "size": size,
            },
        )
