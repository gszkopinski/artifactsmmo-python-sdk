"""Resources Models."""

from typing import List

from pydantic import BaseModel

from .common import DropRateSchema


class ResourceSchema(BaseModel):
    """Resource Model."""

    name: str
    code: str
    skill: str
    level: int
    drops: List[DropRateSchema]


class ResourceResponseSchema(BaseModel):
    """Resource Response Model."""

    data: ResourceSchema
