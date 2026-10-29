"""Characters schemas."""

from pydantic import BaseModel

from .common import CharacterSchema


class CharacterResponseSchema(BaseModel):
    """CharacterResponseSchema"""

    data: CharacterSchema


class CharacterStatsSchema(BaseModel):
    """CharacterStatsSchema"""

    monsters_killed: dict[str, int] | None = None
    resources_gathered: dict[str, int] | None = None
    items_crafted: dict[str, int] | None = None
    action_counts: dict[str, int] | None = None
    deaths: int | None = None


class CharacterStatsResponseSchema(BaseModel):
    """CharacterStatsResponseSchema"""

    data: CharacterStatsSchema
