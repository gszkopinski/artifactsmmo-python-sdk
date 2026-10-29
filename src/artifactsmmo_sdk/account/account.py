"""Account."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.account import (
    BankResponseSchema,
    MyAccountDetailsSchema,
    PendingItemSchemaPage,
    SimpleItemSchemaPage,
)
from ..models.common import (
    GEOrderHistorySchemaPage,
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

    def get_ge_sell_history(
        self,
        id: Annotated[
            str | None,
            Field(
                description="Order ID to search in your history.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        code: Annotated[
            str | None,
            Field(
                description="Item to search in your history.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, GEOrderHistorySchemaPage | None]:
        """Fetch your transaction history of the last 7 days (buy and sell orders)."""
        return self._request(
            "GET",
            "/my/grandexchange/history",
            GEOrderHistorySchemaPage,
            "Successfully fetched data.",
            params={
                "id": id,
                "code": code,
                "page": page,
                "size": size,
            },
        )

    def get_account_details(
        self,
    ) -> tuple[str, MyAccountDetailsSchema | None]:
        """Fetch account details."""
        return self._request(
            "GET",
            "/my/details",
            MyAccountDetailsSchema,
            "Successfully fetched data.",
        )

    def get_pending_items(
        self,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, PendingItemSchemaPage | None]:
        """Retrieve all unclaimed pending items for your account.

        These are items from various sources (achievements, grand exchange, events, etc.)
        that can be claimed by any character on your account using /my/{name}/action/claim/{id}."""
        return self._request(
            "GET",
            "/my/pending_items",
            PendingItemSchemaPage,
            "Successfully fetched pending items.",
            params={
                "page": page,
                "size": size,
            },
        )
