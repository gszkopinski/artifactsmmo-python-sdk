"""Events Models."""

from typing import List

from pydantic import BaseModel

from .maps import MapSchema


class ActiveEventSchema(BaseModel):
    """ActiveEventSchema."""

    name: str
    map: MapSchema
    previous_skin: str
    duration: int
    expiration: str
    created_at: str


class ListActiveEventResponseSchema(BaseModel):
    """List Active Event Response Schema."""

    data: List[ActiveEventSchema]
    total: int
    page: int
    size: int
    pages: int
