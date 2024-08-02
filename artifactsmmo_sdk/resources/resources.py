"""Resources."""

import requests

from ..models.resources import ResourceResponseSchema


class Resources:
    """Resources."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def get_resource(self, x: int, y: int) -> ResourceResponseSchema:
        """Retrieve the details of a resource."""
        response = self.session.get(
            url=f"{self.api_url}/resources/{x}/{y}",
        )

        response.raise_for_status()

        return ResourceResponseSchema.model_validate(response.json())
