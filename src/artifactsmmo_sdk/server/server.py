"""Server."""

from ..base import BaseModule
from ..models.server import (
    StatusResponseSchema,
)


class Server(BaseModule):
    """Server."""

    def get_server_details(
        self,
    ) -> tuple[str, StatusResponseSchema | None]:
        """Return the status of the game server."""
        return self._request(
            "GET",
            "/",
            StatusResponseSchema,
            "Successfully fetched status.",
        )
