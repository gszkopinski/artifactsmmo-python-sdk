"""Badges."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.badges import (
    BadgeResponseSchema,
    StaticDataPage_BadgeSchema_,
)


class Badges(BaseModule):
    """Badges."""

    def get_all_badges(
        self,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_BadgeSchema_ | None]:
        """List of all badges."""
        return self._request(
            "GET",
            "/badges",
            StaticDataPage_BadgeSchema_,
            "Successfully fetched badges.",
            params={
                "page": page,
                "size": size,
            },
        )

    def get_badge(
        self,
        code: Annotated[
            str, Field(description="The code of the badge.", pattern="^[a-zA-Z0-9_-]+$")
        ],
    ) -> tuple[str, BadgeResponseSchema | None]:
        """Retrieve the details of a badge."""
        return self._request(
            "GET",
            f"/badges/{code}",
            BadgeResponseSchema,
            "Successfully fetched badge.",
            {
                404: "badge not found.",
            },
        )
