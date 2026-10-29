"""Effects."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.effects import (
    StaticDataPage_EffectSchema_,
)


class Effects(BaseModule):
    """Effects."""

    def get_all_effects(
        self,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_EffectSchema_ | None]:
        """List of all effects. Effects are used by equipment, tools, runes, consumables and monsters. An effect is an action that produces an effect on the game."""
        return self._request(
            "GET",
            "/effects",
            StaticDataPage_EffectSchema_,
            "Successfully fetched effects.",
            params={
                "page": page,
                "size": size,
            },
        )
