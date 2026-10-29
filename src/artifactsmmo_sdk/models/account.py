"""Account schemas."""

from datetime import datetime

from pydantic import BaseModel

from .common import (
    AccountStatus,
    PendingItemSchema,
    RateLimitScopeSchema,
    SimpleItemSchema,
)


class BankSchema(BaseModel):
    """BankSchema"""

    slots: int
    expansions: int
    next_expansion_cost: int
    gold: int


class BankResponseSchema(BaseModel):
    """BankResponseSchema"""

    data: BankSchema


class PendingItemSchemaPage(BaseModel):
    """DataPage[PendingItemSchema]"""

    data: list[PendingItemSchema]
    total: int
    page: int
    size: int
    pages: int


class SimpleItemSchemaPage(BaseModel):
    """DataPage[SimpleItemSchema]"""

    data: list[SimpleItemSchema]
    total: int
    page: int
    size: int
    pages: int


class MyAccountDetails(BaseModel):
    """MyAccountDetails"""

    username: str
    email: str
    member: bool
    member_expiration: datetime | None = None
    status: AccountStatus
    badges: list[str] | None = None
    skins: list[str]
    gems: int
    member_token: int | None = None
    achievements_points: int
    banned: bool
    ban_reason: str | None = None


class MyAccountDetailsSchema(BaseModel):
    """MyAccountDetailsSchema"""

    data: MyAccountDetails


class RateLimitsDataSchema(BaseModel):
    """RateLimitsDataSchema"""

    account: RateLimitScopeSchema
    data: RateLimitScopeSchema
    action: RateLimitScopeSchema
    simulation: RateLimitScopeSchema
    assistant: RateLimitScopeSchema | None = None


class RateLimitsSchema(BaseModel):
    """RateLimitsSchema"""

    data: RateLimitsDataSchema
