"""Items."""

import requests

from ..models.items import SingleItemResponseSchema


class Items:
    """Items."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def get_item(self, code: str) -> SingleItemResponseSchema:
        """Retrieve the details of a item."""
        response = self.session.get(
            url=f"{self.api_url}/items/{code}",
        )

        response.raise_for_status()

        return SingleItemResponseSchema.model_validate(response.json())
