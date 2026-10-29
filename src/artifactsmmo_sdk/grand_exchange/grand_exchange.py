"""GrandExchange."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.common import (
    GEOrderHistorySchemaPage,
    GEOrderSchemaPage,
    GEOrderType,
    ItemType,
)


class GrandExchange(BaseModule):
    """GrandExchange."""

    def get_ge_history(
        self,
        code: Annotated[
            str, Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        account: Annotated[
            str | None,
            Field(
                description="Account involved in the transaction (matches either seller or buyer).",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, GEOrderHistorySchemaPage | None]:
        """Fetch the transaction history of the item for the last 7 days (buy and sell orders)."""
        return self._request(
            "GET",
            f"/grandexchange/history/{code}",
            GEOrderHistorySchemaPage,
            "Successfully fetched item history.",
            {
                404: "item history not found.",
            },
            params={
                "account": account,
                "page": page,
                "size": size,
            },
        )

    def get_ge_orders(
        self,
        code: Annotated[
            str | None,
            Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$"),
        ] = None,
        account: Annotated[
            str | None,
            Field(
                description="The account that sells or buys items.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        type: Annotated[
            GEOrderType | None, Field(description="Filter by order type (sell or buy).")
        ] = None,
        item_type: Annotated[
            ItemType | None, Field(description="Filter by item type.")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, GEOrderSchemaPage | None]:
        """Fetch all orders (sell and buy orders).

        Use the `type` parameter to filter by order type; when using `account`, `type`
        is required to keep account searches explicit."""
        return self._request(
            "GET",
            "/grandexchange/orders",
            GEOrderSchemaPage,
            "Successfully fetched GE orders.",
            params={
                "code": code,
                "account": account,
                "type": type,
                "item_type": item_type,
                "page": page,
                "size": size,
            },
        )
