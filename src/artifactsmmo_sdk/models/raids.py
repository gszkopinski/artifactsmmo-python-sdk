"""Raids schemas."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from .common import SimpleItemSchema


class RaidLeaderboardEntrySchema(BaseModel):
    """RaidLeaderboardEntrySchema"""

    position: int
    account: str
    points: int


class RaidLeaderboardEntrySchemaPage(BaseModel):
    """DataPage[RaidLeaderboardEntrySchema]"""

    data: list[RaidLeaderboardEntrySchema]
    total: int
    page: int
    size: int
    pages: int


class RaidDamageRewardSchema(BaseModel):
    """RaidDamageRewardSchema"""

    damage_per_reward: int
    max_rewards: int | None = None
    items: list[SimpleItemSchema] | None = None


class RaidInstanceResult(str, Enum):
    """RaidInstanceResult."""

    SUCCESS = "success"
    FAILURE = "failure"


class RaidStatus(str, Enum):
    """RaidStatus."""

    UPCOMING = "upcoming"
    ACTIVE = "active"
    FINISHED_SUCCESS = "finished_success"
    FINISHED_FAILURE = "finished_failure"


class RaidInstanceSchema(BaseModel):
    """RaidInstanceSchema"""

    starts_at: datetime
    ends_at: datetime
    status: RaidStatus
    total_hp: int
    remaining_hp: int
    participant_count: int | None = None
    ended_at: datetime | None = None
    result: RaidInstanceResult | None = None
    rewards_distributed_at: datetime | None = None


class RaidRankRewardSchema(BaseModel):
    """RaidRankRewardSchema"""

    min_rank: int
    max_rank: int
    items: list[SimpleItemSchema] | None = None


class RaidRewardsSchema(BaseModel):
    """RaidRewardsSchema"""

    damage_rewards: list[RaidDamageRewardSchema] | None = None
    leaderboard: list[RaidRankRewardSchema] | None = None


class RaidWeekday(str, Enum):
    """RaidWeekday."""

    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class RaidScheduleSchema(BaseModel):
    """RaidScheduleSchema"""

    weekdays: list[RaidWeekday]
    start_hour_utc: int | None = None
    start_minute_utc: int | None = None
    duration_hours: int | None = None


class RaidSchema(BaseModel):
    """RaidSchema"""

    code: str
    name: str
    description: str | None = None
    monster: str
    schedule: RaidScheduleSchema
    rewards: RaidRewardsSchema | None = None
    status: RaidStatus
    next_start_at: datetime
    participant_count: int | None = None
    active_instance: RaidInstanceSchema | None = None
    latest_instance: RaidInstanceSchema | None = None


class RaidResponseSchema(BaseModel):
    """RaidResponseSchema"""

    data: RaidSchema


class StaticDataPage_RaidSchema_(BaseModel):
    """StaticDataPage[RaidSchema]"""

    data: list[RaidSchema]
    total: int
    page: int
    size: int
    pages: int
