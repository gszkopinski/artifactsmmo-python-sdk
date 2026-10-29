"""Resources."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.resources import (
    ListResourceResponseSchema,
    ResourceResponseSchema,
    SkillEnum,
)


class Resources(BaseModule):
    """Resources."""

    def get_resource(
        self,
        code: Annotated[
            str,
            Field(description="The code of the monster.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, ResourceResponseSchema | None]:
        """Retrieve the details of a resource."""
        return self._request(
            "GET",
            f"/resources/{code}",
            ResourceResponseSchema,
            "Successfully fetched resource.",
            {
                404: "Ressource not found.",
            },
        )

    def get_all_resources(
        self,
        drop: Annotated[
            str, Field(description="Item code of the drop.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        max_level: Annotated[int, Field(description="Monster maximum level.", ge=0)],
        min_level: Annotated[int, Field(description="Monster minimum level.", ge=0)],
        skill: Annotated[SkillEnum, Field(description="The code of the skill.")],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, ListResourceResponseSchema | None]:
        """Return resources."""
        return self._request(
            "GET",
            "/resources",
            ListResourceResponseSchema,
            "",
            {
                404: "Ressources not found.",
            },
            params={
                "page": page,
                "size": size,
                "drop": drop or None,
                "max_level": max_level or None,
                "min_level": min_level or None,
                "skill": skill or None,
            },
        )
