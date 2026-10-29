"""Tasks schemas."""

from enum import Enum

from pydantic import BaseModel

from .common import RewardsSchema, TaskType


class Skill(str, Enum):
    """Skill."""

    WEAPONCRAFTING = "weaponcrafting"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    COOKING = "cooking"
    WOODCUTTING = "woodcutting"
    MINING = "mining"
    ALCHEMY = "alchemy"
    FISHING = "fishing"


class TaskFullSchema(BaseModel):
    """TaskFullSchema"""

    code: str
    level: int
    type: TaskType
    min_quantity: int
    max_quantity: int
    skill: str | None = None
    rewards: RewardsSchema


class StaticDataPage_TaskFullSchema_(BaseModel):
    """StaticDataPage[TaskFullSchema]"""

    data: list[TaskFullSchema]
    total: int
    page: int
    size: int
    pages: int
