"""Events."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.common import (
    MapContentType,
)
from ..models.events import (
    StaticDataPage_ActiveEventSchema_,
    StaticDataPage_EventSchema_,
)


class Events(BaseModule):
    """Events."""

    def get_all_active_events(
        self,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_ActiveEventSchema_ | None]:
        """Fetch active events details."""
        return self._request(
            "GET",
            "/events/active",
            StaticDataPage_ActiveEventSchema_,
            "Successfully fetched active events.",
            params={
                "page": page,
                "size": size,
            },
        )

    def get_all_events(
        self,
        type: Annotated[
            MapContentType | None, Field(description="Type of events.")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_EventSchema_ | None]:
        """Fetch events details."""
        return self._request(
            "GET",
            "/events",
            StaticDataPage_EventSchema_,
            "Successfully fetched events.",
            params={
                "type": type,
                "page": page,
                "size": size,
            },
        )
