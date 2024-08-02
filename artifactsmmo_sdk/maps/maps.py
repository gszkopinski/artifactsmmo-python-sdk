"""Maps."""

import requests

from ..models.maps import MapResponseSchema


class Maps:
    """Maps."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def get_map(self, x: int, y: int) -> MapResponseSchema:
        """Retrieve the details of a map."""
        response = self.session.get(
            url=f"{self.api_url}/maps/{x}/{y}",
        )

        response.raise_for_status()

        return MapResponseSchema.model_validate(response.json())
