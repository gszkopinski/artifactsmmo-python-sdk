"""Grand Exchange."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.grand_exchange import (
    GEItemResponseSchema,
    ListActiveEventResponseSchema,
)


class GrandExchange:
    """Grand Excahnge."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def get_ge_item(
        self,
        code: Annotated[str, Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, GEItemResponseSchema | None]:
        """Retrieve the details of a Grand Exchange item.."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/ge/{code}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched Grand Exchange item.",
                GEItemResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_all_ge_item(
        self,
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[int, Field(description="Page size.", ge=1, le=100, default=50)] = 50,
    ) -> Tuple[str, ListActiveEventResponseSchema | None]:
        """Fetch Grand Exchange items details."""
        try:
            parameters = f"page={page}"
            parameters += f"&size={size}"

            response = self.session.get(
                url=f"{self.api_url}/ge?{parameters}",
            )

            response.raise_for_status()

            return (
                "Fetch Grand Exchange items details.",
                ListActiveEventResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case _:
                    return f"Unknown error: {error}", None
