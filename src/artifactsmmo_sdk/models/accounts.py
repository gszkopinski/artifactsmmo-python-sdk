"""Accounts schemas."""

from datetime import datetime

from pydantic import BaseModel

from .common import AchievementRewardsSchema, AchievementType, CharacterSchema


class AccountAchievementObjectiveSchema(BaseModel):
    """Schema for a single objective within an account achievement, including progress."""

    type: AchievementType
    target: str | None = None
    progress: int | None = None
    total: int


class AccountAchievementSchema(BaseModel):
    """Full achievement data with progress - for API responses."""

    name: str
    code: str
    description: str
    points: int
    objectives: list[AccountAchievementObjectiveSchema]
    rewards: AchievementRewardsSchema
    completed_at: datetime | None = None


class CharactersListSchema(BaseModel):
    """CharactersListSchema"""

    data: list[CharacterSchema]


class AccountAchievementSchemaPage(BaseModel):
    """DataPage[AccountAchievementSchema]"""

    data: list[AccountAchievementSchema]
    total: int
    page: int
    size: int
    pages: int
