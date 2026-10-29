"""Account schemas."""

from datetime import datetime
from enum import Enum
from typing import Literal

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


class CheckoutResponseSchema(BaseModel):
    """Checkout session response."""

    checkout_url: str
    session_id: str


class CheckoutResponseWrapperSchema(BaseModel):
    """CheckoutResponseWrapperSchema"""

    data: CheckoutResponseSchema


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


class MemberTokenSubscriptionResponseDataSchema(BaseModel):
    """MemberTokenSubscriptionResponseDataSchema"""

    member: bool
    member_expiration: datetime
    member_token: int


class MemberTokenSubscriptionResponseSchema(BaseModel):
    """MemberTokenSubscriptionResponseSchema"""

    data: MemberTokenSubscriptionResponseDataSchema


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


class PurchaseType(str, Enum):
    """PurchaseType."""

    SUBSCRIPTION = "subscription"
    GEM_PACK = "gem_pack"


class PurchaseHistorySchema(BaseModel):
    """PurchaseHistorySchema"""

    type: PurchaseType
    description: str
    amount: int
    gems_credited: int | None = None
    created_at: datetime


class PurchaseHistoryListResponseSchema(BaseModel):
    """PurchaseHistoryListResponseSchema"""

    data: list[PurchaseHistorySchema]


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


class StripeSubscriptionPlan(str, Enum):
    """StripeSubscriptionPlan."""

    MONTHLY = "monthly"
    ANNUAL = "annual"


class SubscriptionPlan(str, Enum):
    """SubscriptionPlan."""

    MONTHLY = "monthly"
    ANNUAL = "annual"
    PREPAID = "prepaid"


class SubscriptionSchema(BaseModel):
    """SubscriptionSchema"""

    plan: SubscriptionPlan
    purchase_source: Literal["stripe", "gems", "member_token", "mixed"]
    status: str
    current_period_start: datetime
    current_period_end: datetime
    created_at: datetime
    cancelled_at: datetime | None = None


class SubscriptionResponseSchema(BaseModel):
    """SubscriptionResponseSchema"""

    data: SubscriptionSchema
