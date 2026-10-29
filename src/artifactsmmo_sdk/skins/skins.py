"""Skins."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.skins import (
    StaticDataPage_SkinSchema_,
)


class Skins(BaseModule):
    """Skins."""

    def get_all_skins(
        self,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_SkinSchema_ | None]:
        """List of all skins available in the game."""
        return self._request(
            "GET",
            "/skins",
            StaticDataPage_SkinSchema_,
            "Successfully fetched skins.",
            params={
                "page": page,
                "size": size,
            },
        )
