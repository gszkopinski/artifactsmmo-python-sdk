"""Server schemas."""

from datetime import datetime

from pydantic import BaseModel

from .common import RewardType


class RateLimitSchema(BaseModel):
    """RateLimitSchema"""

    type: str
    value: str


class StatusSeasonRewardSchema(BaseModel):
    """Season reward as shown in server details (without season number since it's implied)."""

    code: str
    type: RewardType
    description: str
    required_points: int
    quantity: int | None = None
    member_required: bool | None = None
    first_only: bool | None = None


class SeasonSchema(BaseModel):
    """SeasonSchema"""

    name: str | None = None
    number: int | None = None
    start_date: datetime | None = None
    rewards: list[StatusSeasonRewardSchema]


class StatusSchema(BaseModel):
    """StatusSchema"""

    version: str
    server_time: datetime
    max_level: int
    max_skill_level: int
    characters_online: int
    season: SeasonSchema | None = None
    rate_limits: list[RateLimitSchema]


class StatusResponseSchema(BaseModel):
    """StatusResponseSchema"""

    data: StatusSchema
