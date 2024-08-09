"""Maps Schemas."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from .common import MapContentSchema


class MapContentTypeSchema(str, Enum):
    """Map Content Type Schema."""

    MONSTER = "monster"
    RESOURCE = "resource"
    WORKSHOP = "workshop"
    BANK = "bank"
    GRAND_EXCHANGE = "grand_exchange"
    TASKS_MASTER = "tasks_master"


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
