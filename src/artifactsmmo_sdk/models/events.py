"""Events schemas."""

from datetime import datetime

from pydantic import BaseModel

from .common import ActiveEventSchema, MapContentType, TransitionSchema


class EventContentSchema(BaseModel):
    """EventContentSchema"""

    type: MapContentType
    code: str


class EventMapSchema(BaseModel):
    """EventMapSchema"""

    map_id: int
    x: int
    y: int
    layer: str
    skin: str


class EventSchema(BaseModel):
    """EventSchema"""

    name: str
    code: str
    content: EventContentSchema | None = None
    maps: list[EventMapSchema]
    duration: int
    rate: int
    cooldown: int | None = None
    cooldown_expiration: datetime | None = None
    price: int | None = None
    transition: TransitionSchema | None = None


class StaticDataPage_ActiveEventSchema_(BaseModel):
    """StaticDataPage[ActiveEventSchema]"""

    data: list[ActiveEventSchema]
    total: int
    page: int
    size: int
    pages: int


class StaticDataPage_EventSchema_(BaseModel):
    """StaticDataPage[EventSchema]"""

    data: list[EventSchema]
    total: int
    page: int
    size: int
    pages: int
