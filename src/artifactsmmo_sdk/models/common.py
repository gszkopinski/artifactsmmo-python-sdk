"""Common schemas."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class AccountStatus(str, Enum):
    """AccountStatus."""

    STANDARD = "standard"
    FOUNDER = "founder"
    GOLD_FOUNDER = "gold_founder"
    VIP_FOUNDER = "vip_founder"
    GOBLIN1 = "goblin1"


class RewardItemSchema(BaseModel):
    """Schema for a single item reward."""

    code: str
    quantity: int


class AchievementRewardsSchema(BaseModel):
    """Schema for achievement rewards including gold and items."""

    gold: int | None = None
    items: list[RewardItemSchema] | None = None


class AchievementType(str, Enum):
    """AchievementType."""

    COMBAT_KILL = "combat_kill"
    COMBAT_DROP = "combat_drop"
    COMBAT_LEVEL = "combat_level"
    GATHERING = "gathering"
    CRAFTING = "crafting"
    RECYCLING = "recycling"
    TASK = "task"
    OTHER = "other"
    USE = "use"
    NPC_BUY = "npc_buy"
    NPC_SELL = "npc_sell"


class GEOrderHistorySchema(BaseModel):
    """GEOrderHistorySchema"""

    order_id: str
    seller: str
    buyer: str
    code: str
    quantity: int
    price: int
    sold_at: datetime


class GEOrderHistorySchemaPage(BaseModel):
    """DataPage[GEOrderHistorySchema]"""

    data: list[GEOrderHistorySchema]
    total: int
    page: int
    size: int
    pages: int


class GEOrderType(str, Enum):
    """GEOrderType."""

    SELL = "sell"
    BUY = "buy"


class GEOrderSchema(BaseModel):
    """GEOrderSchema"""

    id: str
    type: GEOrderType
    account: str | None = None
    code: str
    quantity: int
    price: int
    created_at: datetime


class GEOrderSchemaPage(BaseModel):
    """DataPage[GEOrderSchema]"""

    data: list[GEOrderSchema]
    total: int
    page: int
    size: int
    pages: int


class PendingItemSource(str, Enum):
    """PendingItemSource."""

    ACHIEVEMENT = "achievement"
    GRAND_EXCHANGE = "grand_exchange"
    ADMIN = "admin"
    EVENT = "event"
    RAID = "raid"
    OTHER = "other"


class SimpleItemSchema(BaseModel):
    """SimpleItemSchema"""

    code: str
    quantity: int


class PendingItemSchema(BaseModel):
    """Schema for pending items that can be claimed by any character."""

    id: str
    account: str
    source: PendingItemSource
    source_id: str | None = None
    description: str
    gold: int | None = None
    items: list[SimpleItemSchema] | None = None
    created_at: datetime
    claimed_at: datetime | None = None


class RateLimitWindowSchema(BaseModel):
    """RateLimitWindowSchema"""

    limit: int
    remaining: int
    reset: datetime


class RateLimitScopeSchema(BaseModel):
    """RateLimitScopeSchema"""

    second: RateLimitWindowSchema | None = None
    minute: RateLimitWindowSchema | None = None
    hour: RateLimitWindowSchema | None = None
    day: RateLimitWindowSchema | None = None


class ResponseSchema(BaseModel):
    """ResponseSchema"""

    message: str


class RewardType(str, Enum):
    """RewardType."""

    BADGE = "badge"
    SKIN = "skin"
    GOLD = "gold"
    ITEM = "item"
