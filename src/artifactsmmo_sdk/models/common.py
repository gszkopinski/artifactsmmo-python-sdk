"""Common schemas."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class ConditionOperator(str, Enum):
    """ConditionOperator."""

    EQ = "eq"
    NE = "ne"
    GT = "gt"
    LT = "lt"
    COST = "cost"
    HAS_ITEM = "has_item"
    ACHIEVEMENT_UNLOCKED = "achievement_unlocked"


class ConditionSchema(BaseModel):
    """ConditionSchema"""

    code: str
    operator: ConditionOperator
    value: int


class MapAccessType(str, Enum):
    """MapAccessType."""

    STANDARD = "standard"
    RESTRICTED = "restricted"
    CONDITIONAL = "conditional"
    BLOCKED = "blocked"


class AccessSchema(BaseModel):
    """AccessSchema"""

    type: MapAccessType
    conditions: list[ConditionSchema] | None = None


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


class InventorySlotSchema(BaseModel):
    """InventorySlotSchema"""

    slot: int
    code: str
    quantity: int


class MapLayer(str, Enum):
    """MapLayer."""

    INTERIOR = "interior"
    OVERWORLD = "overworld"
    UNDERGROUND = "underground"


class StorageEffectSchema(BaseModel):
    """StorageEffectSchema"""

    code: str
    value: int


class CharacterSchema(BaseModel):
    """CharacterSchema"""

    name: str
    account: str
    skin: str
    level: int
    xp: int
    max_xp: int
    gold: int
    speed: int
    mining_level: int
    mining_xp: int
    mining_max_xp: int
    woodcutting_level: int
    woodcutting_xp: int
    woodcutting_max_xp: int
    fishing_level: int
    fishing_xp: int
    fishing_max_xp: int
    weaponcrafting_level: int
    weaponcrafting_xp: int
    weaponcrafting_max_xp: int
    gearcrafting_level: int
    gearcrafting_xp: int
    gearcrafting_max_xp: int
    jewelrycrafting_level: int
    jewelrycrafting_xp: int
    jewelrycrafting_max_xp: int
    cooking_level: int
    cooking_xp: int
    cooking_max_xp: int
    alchemy_level: int
    alchemy_xp: int
    alchemy_max_xp: int
    hp: int
    max_hp: int
    haste: int
    critical_strike: int
    wisdom: int
    prospecting: int
    initiative: int
    threat: int
    attack_fire: int
    attack_earth: int
    attack_water: int
    attack_air: int
    dmg: int
    dmg_fire: int
    dmg_earth: int
    dmg_water: int
    dmg_air: int
    res_fire: int
    res_earth: int
    res_water: int
    res_air: int
    effects: list[StorageEffectSchema] | None = None
    x: int
    y: int
    layer: MapLayer
    map_id: int
    cooldown: int
    cooldown_expiration: datetime | None = None
    weapon_slot: str
    rune_slot: str
    shield_slot: str
    helmet_slot: str
    body_armor_slot: str
    leg_armor_slot: str
    boots_slot: str
    ring1_slot: str
    ring2_slot: str
    amulet_slot: str
    artifact1_slot: str
    artifact2_slot: str
    artifact3_slot: str
    utility1_slot: str
    utility1_slot_quantity: int
    utility2_slot: str
    utility2_slot_quantity: int
    bag_slot: str
    task: str
    task_type: str
    task_progress: int
    task_total: int
    inventory_max_items: int
    inventory: list[InventorySlotSchema] | None = None


class CraftSkill(str, Enum):
    """CraftSkill."""

    WEAPONCRAFTING = "weaponcrafting"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    COOKING = "cooking"
    WOODCUTTING = "woodcutting"
    MINING = "mining"
    ALCHEMY = "alchemy"


class SimpleItemSchema(BaseModel):
    """SimpleItemSchema"""

    code: str
    quantity: int


class CraftSchema(BaseModel):
    """CraftSchema"""

    skill: CraftSkill | None = None
    level: int | None = None
    items: list[SimpleItemSchema] | None = None
    quantity: int | None = None


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


class MapContentType(str, Enum):
    """MapContentType."""

    MONSTER = "monster"
    RESOURCE = "resource"
    WORKSHOP = "workshop"
    BANK = "bank"
    GRAND_EXCHANGE = "grand_exchange"
    TASKS_MASTER = "tasks_master"
    NPC = "npc"
    RAID = "raid"


class MapContentSchema(BaseModel):
    """MapContentSchema"""

    type: MapContentType
    code: str


class TransitionSchema(BaseModel):
    """TransitionSchema"""

    map_id: int
    x: int
    y: int
    layer: MapLayer
    conditions: list[ConditionSchema] | None = None


class InteractionSchema(BaseModel):
    """InteractionSchema"""

    content: MapContentSchema | None = None
    transition: TransitionSchema | None = None


class SimpleEffectSchema(BaseModel):
    """SimpleEffectSchema"""

    code: str
    value: int
    description: str


class ItemSchema(BaseModel):
    """ItemSchema"""

    name: str
    code: str
    level: int
    type: str
    subtype: str
    description: str
    conditions: list[ConditionSchema] | None = None
    effects: list[SimpleEffectSchema] | None = None
    craft: CraftSchema | None = None
    tradeable: bool
    recyclable: bool | None = None


class MapSchema(BaseModel):
    """MapSchema"""

    map_id: int
    name: str
    skin: str
    x: int
    y: int
    layer: MapLayer
    access: AccessSchema
    interactions: InteractionSchema


class PendingItemSource(str, Enum):
    """PendingItemSource."""

    ACHIEVEMENT = "achievement"
    GRAND_EXCHANGE = "grand_exchange"
    ADMIN = "admin"
    EVENT = "event"
    RAID = "raid"
    OTHER = "other"


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


class RewardsSchema(BaseModel):
    """RewardsSchema"""

    items: list[SimpleItemSchema]
    gold: int


class TaskType(str, Enum):
    """TaskType."""

    MONSTERS = "monsters"
    ITEMS = "items"
