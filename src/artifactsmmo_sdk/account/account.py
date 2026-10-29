"""Account."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.account import (
    BankResponseSchema,
    SimpleItemSchemaPage,
)
from ..models.common import (
    GEOrderSchemaPage,
    GEOrderType,
)


class Account(BaseModule):
    """Account."""

    def get_bank_details(
        self,
    ) -> tuple[str, BankResponseSchema | None]:
        """Fetch bank details."""
        return self._request(
            "GET",
            "/my/bank",
            BankResponseSchema,
            "Successfully fetched data.",
        )

    def get_bank_items(
        self,
        item_code: Annotated[
            str | None,
            Field(
                description="Item to search in your bank.", pattern="^[a-zA-Z0-9_-]+$"
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, SimpleItemSchemaPage | None]:
        """Fetch all items in your bank."""
        return self._request(
            "GET",
            "/my/bank/items",
            SimpleItemSchemaPage,
            "Successfully fetched data.",
            params={
                "item_code": item_code,
                "page": page,
                "size": size,
            },
        )

    def get_ge_sell_orders(
        self,
        code: Annotated[
            str | None,
            Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$"),
        ] = None,
        type: Annotated[
            GEOrderType | None, Field(description="Filter by order type (sell or buy).")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, GEOrderSchemaPage | None]:
        """Fetch your orders details (sell and buy orders)."""
        return self._request(
            "GET",
            "/my/grandexchange/orders",
            GEOrderSchemaPage,
            "Successfully fetched data.",
            params={
                "code": code,
                "type": type,
                "page": page,
                "size": size,
            },
        )
