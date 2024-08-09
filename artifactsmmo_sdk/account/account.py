"""Account."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.actions import (
    ListBankItemsResponseSchema,
    ListBankGoldsResponseSchema,
    ChangePasswordResponseSchema,
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

    def get_bank_items(
        self,
        item_code: Annotated[str, Field(description="Item to search in your bank.", pattern="^[a-zA-Z0-9_-]+$")],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[int, Field(description="Page size.", ge=1, le=100, default=50)] = 50,
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
                ListBankItemsResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Items not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_bank_gold(
        self,
    ) -> Tuple[str, ListBankGoldsResponseSchema | None]:
        """Fetch golds in your bank."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/my/bank/gold",
            )

            response.raise_for_status()

            return (
                "Successfully fetched golds.",
                ListBankGoldsResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case _:
                    return f"Unknown error: {error}", None

    def change_password(
        self,
    ) -> Tuple[str, ChangePasswordResponseSchema | None]:
        """Change your account password. Changing the password reset the account token."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/change_password",
            )

            response.raise_for_status()

            return (
                "Password changed successfully.",
                ChangePasswordResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 458:
                    return "Use a different password.", None
                case _:
                    return f"Unknown error: {error}", None
