"""Achievements schemas."""

from pydantic import BaseModel

from .common import AchievementRewardsSchema, AchievementType


class AchievementObjectiveSchema(BaseModel):
    """Schema for a single objective within an achievement."""

    type: AchievementType
    target: str | None = None
    total: int


class AchievementSchema(BaseModel):
    """Schema for an achievement definition."""

    name: str
    code: str
    description: str
    points: int
    objectives: list[AchievementObjectiveSchema]
    rewards: AchievementRewardsSchema


class AchievementResponseSchema(BaseModel):
    """AchievementResponseSchema"""

    data: AchievementSchema


class StaticDataPage_AchievementSchema_(BaseModel):
    """StaticDataPage[AchievementSchema]"""

    data: list[AchievementSchema]
    total: int
    page: int
    size: int
    pages: int
