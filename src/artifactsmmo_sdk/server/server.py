"""Server."""

import requests

from ..models.server import StatusResponseSchema


class Server:
    """Server."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def status(
        self,
    ) -> StatusResponseSchema:
        """Return the status of the game server."""
        response = self.session.get(
            url=f"{self.api_url}/",
        )

        response.raise_for_status()

        return StatusResponseSchema.model_validate(response.json())
