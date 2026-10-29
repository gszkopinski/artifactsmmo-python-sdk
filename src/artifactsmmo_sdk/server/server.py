"""Server."""

from ..base import BaseModule
from ..models.server import StatusResponseSchema


class Server(BaseModule):
    """Server."""

    def status(
        self,
    ) -> StatusResponseSchema:
        """Return the status of the game server."""
        response = self.session.get(
            url=f"{self.api_url}/",
        )

        response.raise_for_status()

        return StatusResponseSchema.model_validate(response.json())
