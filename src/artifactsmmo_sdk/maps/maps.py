"""Maps."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.maps import ListMapResponseSchema, MapContentTypeSchema, MapResponseSchema


class Maps(BaseModule):
    """Maps."""

    def get_map(
        self,
        x: Annotated[int, Field(description="The position X of the map.")],
        y: Annotated[int, Field(description="The position Y of the map.")],
    ) -> tuple[str, MapResponseSchema | None]:
        """Retrieve the details of a map."""
        return self._request(
            "GET",
            f"/maps/{x}/{y}",
            MapResponseSchema,
            "Successfully fetched map.",
            {
                404: "Map not found.",
            },
        )

    def get_all_maps(
        self,
        content_code: Annotated[
            str,
            Field(description="Content code on the map.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        content_type: Annotated[
            MapContentTypeSchema,
            Field(
                description="Type of content on the map.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, ListMapResponseSchema | None]:
        """Fetch maps details."""
        return self._request(
            "GET",
            "/maps",
            ListMapResponseSchema,
            "Successfully fetched maps details.",
            {
                404: "Maps not found.",
            },
            params={
                "page": page,
                "size": size,
                "content_code": content_code or None,
                "content_type": content_type or None,
            },
        )
