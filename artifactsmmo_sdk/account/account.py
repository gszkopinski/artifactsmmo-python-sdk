"""Account."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.account import (
    AccountDetailsResponseSchema,
    ChangePasswordResponseSchema,
    GEOrderHistoryResponseSchema,
    GEOrderResponseSchema,
    ListBankDetailsResponseSchema,
    ListBankItemsResponseSchema,
)


class Account:
    """Account."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    # -----------------------------------------------------
    # BANK
    # -----------------------------------------------------
    def get_bank_details(
        self,
    ) -> Tuple[str, dict | None]:
        """Fetch your bank details."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/my/bank",
            )

            response.raise_for_status()

            return (
                "Successfully fetched bank details.",
                ListBankDetailsResponseSchema.model_validate(response.json()),
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case _:
                    return f"Unknown error: {error}", None

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
    ) -> Tuple[str, ListBankItemsResponseSchema | None]:
        """Fetch all items in your bank."""
        try:
            parameters = f"item_code={item_code}"
            parameters += f"&page={page}"
            parameters += f"&size={size}"

            response = self.session.get(
                url=f"{self.api_url}/my/bank/items?{parameters}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched items.",
                ListBankItemsResponseSchema.model_validate(response.json()),
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case _:
                    return f"Unknown error: {error}", None

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
    ) -> Tuple[str, GEOrderResponseSchema | None]:
        """Fetch your grand exchange sell orders."""
        try:
            parameters = f"code={item_code}"
            parameters += f"&page={page}"
            parameters += f"&size={size}"

            response = self.session.get(
                url=f"{self.api_url}/my/grandexchange/orders?{parameters}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched grand exchange sell orders.",
                GEOrderResponseSchema.model_validate(response.json()),
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case _:
                    return f"Unknown error: {error}", None

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
    ) -> Tuple[str, GEOrderHistoryResponseSchema | None]:
        """Fetch your grand exchange order history."""
        try:
            parameters = f"code={item_code}"
            parameters += f"&id={id}"
            parameters += f"&page={page}"
            parameters += f"&size={size}"

            response = self.session.get(
                url=f"{self.api_url}/my/grandexchange/history?{parameters}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched data.",
                GEOrderHistoryResponseSchema.model_validate(response.json()),
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case _:
                    return f"Unknown error: {error}", None

    # -----------------------------------------------------
    # ACCOUNT
    # -----------------------------------------------------
    def get_account_details(
        self,
    ) -> Tuple[str, AccountDetailsResponseSchema | None]:
        """Fetch your account details."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/my/details",
            )

            response.raise_for_status()

            return (
                "Successfully fetched account details.",
                AccountDetailsResponseSchema.model_validate(response.json()),
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case _:
                    return f"Unknown error: {error}", None

    # -----------------------------------------------------
    # PASSWORD
    # -----------------------------------------------------
    def change_password(
        self,
        current_password: Annotated[
            str, Field(description="Your password.", pattern="^[^\s]+$", ge=5, le=50)
        ],
        new_password: Annotated[
            str, Field(description="New password.", pattern="^[^\s]+$", ge=5, le=50)
        ],
    ) -> Tuple[str, ChangePasswordResponseSchema | None]:
        """Change your account password. Changing the password reset the account token."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/change_password",
                json={
                    "current_password": current_password,
                    "new_password": new_password,
                },
            )

            response.raise_for_status()

            return (
                "Password changed successfully.",
                ChangePasswordResponseSchema.model_validate(response.json()),
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 422:
                    return (
                        "Request could not be processed due to an invalid payload.",
                        None,
                    )
                case 458:
                    return "Use a different password.", None
                case 459:
                    return "The current password you entered is invalid.", None
                case _:
                    return f"Unknown error: {error}", None
