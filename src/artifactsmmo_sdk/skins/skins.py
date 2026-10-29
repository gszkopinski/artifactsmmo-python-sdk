"""Skins."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.skins import (
    SkinResponseSchema,
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

    def get_skin(
        self,
        code: Annotated[
            str, Field(description="The code of the skin.", pattern="^[a-zA-Z0-9_-]+$")
        ],
    ) -> tuple[str, SkinResponseSchema | None]:
        """Retrieve the details of a skin."""
        return self._request(
            "GET",
            f"/skins/{code}",
            SkinResponseSchema,
            "Successfully fetched skin.",
            {
                404: "skin not found.",
            },
        )
