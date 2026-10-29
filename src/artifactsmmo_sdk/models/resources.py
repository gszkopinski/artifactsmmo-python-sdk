"""Resources schemas."""

from enum import Enum

from pydantic import BaseModel

from .common import DropRateSchema


class GatheringSkill(str, Enum):
    """GatheringSkill."""

    MINING = "mining"
    WOODCUTTING = "woodcutting"
    FISHING = "fishing"
    ALCHEMY = "alchemy"


class ResourceSchema(BaseModel):
    """ResourceSchema"""

    name: str
    code: str
    skill: GatheringSkill
    level: int
    drops: list[DropRateSchema]


class ResourceResponseSchema(BaseModel):
    """ResourceResponseSchema"""

    data: ResourceSchema


class StaticDataPage_ResourceSchema_(BaseModel):
    """StaticDataPage[ResourceSchema]"""

    data: list[ResourceSchema]
    total: int
    page: int
    size: int
    pages: int
