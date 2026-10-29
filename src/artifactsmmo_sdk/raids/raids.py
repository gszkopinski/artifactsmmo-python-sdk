"""Raids."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.raids import (
    StaticDataPage_RaidSchema_,
)


class Raids(BaseModule):
    """Raids."""

    def get_all_raids(
        self,
        name: Annotated[
            str | None,
            Field(
                description="Name of the raid.",
                pattern="^[a-zA-Z0-9_-]+(\\s[a-zA-Z0-9_-]+)*\\s?$",
            ),
        ] = None,
        active: Annotated[
            bool | None, Field(description="Filter raids by active status.")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_RaidSchema_ | None]:
        """Fetch the list of all raids."""
        return self._request(
            "GET",
            "/raids",
            StaticDataPage_RaidSchema_,
            "Successfully fetched raids.",
            params={
                "name": name,
                "active": active,
                "page": page,
                "size": size,
            },
        )
