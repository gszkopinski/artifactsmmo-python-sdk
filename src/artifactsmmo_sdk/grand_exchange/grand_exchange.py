"""Grand Exchange."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.grand_exchange import (
    GEItemResponseSchema,
    ListActiveEventResponseSchema,
)


class GrandExchange(BaseModule):
    """Grand Excahnge."""

    def get_ge_item(
        self,
        code: Annotated[
            str, Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$")
        ],
    ) -> tuple[str, GEItemResponseSchema | None]:
        """Retrieve the details of a Grand Exchange item.."""
        return self._request(
            "GET",
            f"/ge/{code}",
            GEItemResponseSchema,
            "Successfully fetched Grand Exchange item.",
            {
                404: "Item not found.",
            },
        )

    def get_all_ge_item(
        self,
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, ListActiveEventResponseSchema | None]:
        """Fetch Grand Exchange items details."""
        return self._request(
            "GET",
            "/ge",
            ListActiveEventResponseSchema,
            "Fetch Grand Exchange items details.",
            {
                404: "Item not found.",
            },
            params={
                "page": page,
                "size": size,
            },
        )
