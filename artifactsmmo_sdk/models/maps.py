"""Maps Schemas."""

from typing import Optional

from pydantic import BaseModel

from .common import MapContentSchema


# Map Schema
class MapSchema(BaseModel):
    """Map Schema."""

    name: str
    skin: str
    x: int
    y: int
    content: Optional[MapContentSchema] = None


# Map Response Schema
class MapResponseSchema(BaseModel):
    """Map Response Schema."""

    data: MapSchema
