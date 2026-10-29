"""Events."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.events import ListActiveEventResponseSchema


class Events(BaseModule):
    """Events."""

    def get_all_active_events(
        self,
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, ListActiveEventResponseSchema | None]:
        """Fetch events details."""
        return self._request(
            "GET",
            "/events/active",
            ListActiveEventResponseSchema,
            "Successfully fetched events details.",
            {
                404: "Events not found..",
            },
            params={
                "page": page,
                "size": size,
            },
        )
