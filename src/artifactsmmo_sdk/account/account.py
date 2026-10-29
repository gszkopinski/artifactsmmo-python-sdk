"""Account."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.account import (
    BankResponseSchema,
    DataPage_SimpleItemSchema_,
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
        page: Annotated[int | None, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int | None, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, DataPage_SimpleItemSchema_ | None]:
        """Fetch all items in your bank."""
        return self._request(
            "GET",
            "/my/bank/items",
            DataPage_SimpleItemSchema_,
            "Successfully fetched data.",
            params={
                "item_code": item_code,
                "page": page,
                "size": size,
            },
        )
