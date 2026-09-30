"""Events Models."""

from pydantic import BaseModel

from .maps import MapSchema


class ActiveEventSchema(BaseModel):
    """ActiveEventSchema."""

    name: str
    code: str
    map: MapSchema
    previous_skin: str
    duration: int
    expiration: str
    created_at: str


class ListActiveEventResponseSchema(BaseModel):
    """List Active Event Response Schema."""

    data: list[ActiveEventSchema]
    total: int
    page: int
    size: int
    pages: int
