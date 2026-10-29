"""Badges."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.badges import (
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
