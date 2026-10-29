"""Maps."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.common import (
    MapContentType,
    MapLayer,
)
from ..models.maps import (
    MapResponseSchema,
    StaticDataPage_MapSchema_,
)


class Maps(BaseModule):
    """Maps."""

    def get_all_maps(
        self,
        layer: Annotated[
            MapLayer | None, Field(description="Filter maps by layer.")
        ] = None,
        content_type: Annotated[
            MapContentType | None, Field(description="Type of maps.")
        ] = None,
        content_code: Annotated[
            str | None,
            Field(description="Content code on the map.", pattern="^[a-zA-Z0-9_-]+$"),
        ] = None,
        hide_blocked_maps: Annotated[
            bool | None,
            Field(
                description="When true, excludes maps with access_type 'blocked' from the results."
            ),
        ] = None,
        hide_event: Annotated[
            bool | None,
            Field(description="When true, does not overlay active events on maps."),
        ] = None,
        transition: Annotated[
            bool | None,
            Field(
                description="Filter maps by transition. True returns only maps with transitions, False returns only maps without."
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_MapSchema_ | None]:
        """Fetch maps details."""
        return self._request(
            "GET",
            "/maps",
            StaticDataPage_MapSchema_,
            "Successfully fetched maps.",
            params={
                "layer": layer,
                "content_type": content_type,
                "content_code": content_code,
                "hide_blocked_maps": hide_blocked_maps,
                "hide_event": hide_event,
                "transition": transition,
                "page": page,
                "size": size,
            },
        )

    def get_layer_maps(
        self,
        layer: Annotated[
            MapLayer,
            Field(
                description="The layer of the map (interior, overworld, underground)."
            ),
        ],
        content_type: Annotated[
            MapContentType | None, Field(description="Type of maps.")
        ] = None,
        content_code: Annotated[
            str | None,
            Field(description="Content code on the map.", pattern="^[a-zA-Z0-9_-]+$"),
        ] = None,
        hide_blocked_maps: Annotated[
            bool | None,
            Field(
                description="When true, excludes maps with access_type 'blocked' from the results."
            ),
        ] = None,
        hide_event: Annotated[
            bool | None,
            Field(description="When true, does not overlay active events on maps."),
        ] = None,
        transition: Annotated[
            bool | None,
            Field(
                description="Filter maps by transition. True returns only maps with transitions, False returns only maps without."
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_MapSchema_ | None]:
        """Fetch maps details."""
        return self._request(
            "GET",
            f"/maps/{layer}",
            StaticDataPage_MapSchema_,
            "Successfully fetched maps.",
            params={
                "content_type": content_type,
                "content_code": content_code,
                "hide_blocked_maps": hide_blocked_maps,
                "hide_event": hide_event,
                "transition": transition,
                "page": page,
                "size": size,
            },
        )

    def get_map(
        self,
        layer: Annotated[
            MapLayer,
            Field(
                description="The layer of the map (interior, overworld, underground)."
            ),
        ],
        x: Annotated[int, Field(description="The position x of the map.")],
        y: Annotated[int, Field(description="The position y of the map.")],
    ) -> tuple[str, MapResponseSchema | None]:
        """Retrieve the details of a map by layer and coordinates."""
        return self._request(
            "GET",
            f"/maps/{layer}/{x}/{y}",
            MapResponseSchema,
            "Successfully fetched map.",
            {
                404: "map not found.",
            },
        )
