"""Maps Schemas."""

from typing import List, Optional

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


class ListMapResponseSchema(BaseModel):
    """List Map Response Schema."""

    data: List[MapSchema]
    total: int
    page: int
    size: int
    pages: int
