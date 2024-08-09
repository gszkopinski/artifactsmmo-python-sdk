"""Resources Models."""

from enum import Enum
from typing import List

from pydantic import BaseModel

from .common import DropRateSchema


class SkillEnum(str, Enum):
    """Skill Enum."""

    MINING = "mining"
    WOODCUTTING = "woodcutting"
    FISHING = "fishing"


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


class ListResourceResponseSchema(BaseModel):
    """List Resource Response Schema."""

    data: List[ResourceSchema]
    total: int
    page: int
    size: int
    pages: int
