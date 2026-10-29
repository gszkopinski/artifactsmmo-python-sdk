"""Resources."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.resources import (
    GatheringSkill,
    ResourceResponseSchema,
    StaticDataPage_ResourceSchema_,
)


class Resources(BaseModule):
    """Resources."""

    def get_all_resources(
        self,
        min_level: Annotated[
            int | None, Field(description="Minimum level.", ge=0)
        ] = None,
        max_level: Annotated[
            int | None, Field(description="Maximum level.", ge=0)
        ] = None,
        skill: Annotated[
            GatheringSkill | None, Field(description="Skill of resources.")
        ] = None,
        drop: Annotated[
            str | None,
            Field(description="Item code of the drop.", pattern="^[a-zA-Z0-9_-]+$"),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_ResourceSchema_ | None]:
        """Fetch resources details."""
        return self._request(
            "GET",
            "/resources",
            StaticDataPage_ResourceSchema_,
            "Successfully fetched resources.",
            params={
                "min_level": min_level,
                "max_level": max_level,
                "skill": skill,
                "drop": drop,
                "page": page,
                "size": size,
            },
        )

    def get_resource(
        self,
        code: Annotated[
            str,
            Field(description="The code of the resource.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, ResourceResponseSchema | None]:
        """Retrieve the details of a resource."""
        return self._request(
            "GET",
            f"/resources/{code}",
            ResourceResponseSchema,
            "Successfully fetched resource.",
            {
                404: "resource not found.",
            },
        )
