"""Account."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.account import (
    AccountDetailsResponseSchema,
    ChangePasswordResponseSchema,
    GEOrderHistoryResponseSchema,
    GEOrderResponseSchema,
    ListBankDetailsResponseSchema,
    ListBankItemsResponseSchema,
)


class Account(BaseModule):
    """Account."""

    # -----------------------------------------------------
    # BANK
    # -----------------------------------------------------
    def get_bank_details(
        self,
    ) -> tuple[str, ListBankDetailsResponseSchema | None]:
        """Fetch your bank details."""
        return self._request(
            "GET",
            "/my/bank",
            ListBankDetailsResponseSchema,
            "Successfully fetched bank details.",
        )

    def get_bank_items(
        self,
        item_code: Annotated[
            str,
            Field(
                description="Item to search in your bank.", pattern="^[a-zA-Z0-9_-]+$"
            ),
        ],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, ListBankItemsResponseSchema | None]:
        """Fetch all items in your bank."""
        return self._request(
            "GET",
            "/my/bank/items",
            ListBankItemsResponseSchema,
            "Successfully fetched items.",
            params={
                "item_code": item_code,
                "page": page,
                "size": size,
            },
        )

    # -----------------------------------------------------
    # GRAND EXCHANGE
    # -----------------------------------------------------
    def get_ge_sell_orders(
        self,
        item_code: Annotated[
            str, Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, GEOrderResponseSchema | None]:
        """Fetch your grand exchange sell orders."""
        return self._request(
            "GET",
            "/my/grandexchange/orders",
            GEOrderResponseSchema,
            "Successfully fetched grand exchange sell orders.",
            params={
                "code": item_code,
                "page": page,
                "size": size,
            },
        )

    def get_ge_sell_history(
        self,
        item_code: Annotated[
            str,
            Field(
                description="Item to search in your history.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ],
        id: Annotated[
            str,
            Field(
                description="Order ID to search in your history.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, GEOrderHistoryResponseSchema | None]:
        """Fetch your grand exchange order history."""
        return self._request(
            "GET",
            "/my/grandexchange/history",
            GEOrderHistoryResponseSchema,
            "Successfully fetched data.",
            params={
                "code": item_code,
                "id": id,
                "page": page,
                "size": size,
            },
        )

    # -----------------------------------------------------
    # ACCOUNT
    # -----------------------------------------------------
    def get_account_details(
        self,
    ) -> tuple[str, AccountDetailsResponseSchema | None]:
        """Fetch your account details."""
        return self._request(
            "GET",
            "/my/details",
            AccountDetailsResponseSchema,
            "Successfully fetched account details.",
        )

    # -----------------------------------------------------
    # PASSWORD
    # -----------------------------------------------------
    def change_password(
        self,
        current_password: Annotated[
            str, Field(description="Your password.", pattern=r"^[^\s]+$", ge=5, le=50)
        ],
        new_password: Annotated[
            str, Field(description="New password.", pattern=r"^[^\s]+$", ge=5, le=50)
        ],
    ) -> tuple[str, ChangePasswordResponseSchema | None]:
        """Change your account password. Changing the password reset the account token."""
        return self._request(
            "POST",
            "/my/change_password",
            ChangePasswordResponseSchema,
            "Password changed successfully.",
            {
                458: "Use a different password.",
                459: "The current password you entered is invalid.",
            },
            json={
                "current_password": current_password,
                "new_password": new_password,
            },
        )
