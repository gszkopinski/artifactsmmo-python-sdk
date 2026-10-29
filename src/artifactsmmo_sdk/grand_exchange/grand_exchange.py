"""GrandExchange."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.common import (
    GEOrderHistorySchemaPage,
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
