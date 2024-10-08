"""Characters Schemas."""

from enum import Enum
from typing import List, Optional, Any

from pydantic import BaseModel

from .characters import CharacterSchema
from .common import MapContentSchema


class CooldownReasonEnum(str, Enum):
    """Cooldown Reason Enum."""

    MOVEMENT = "movement"
    FIGHT = "fight"
    CRAFTING = "crafting"
    GATHERING = "gathering"
    BUY_GE = "buy_ge"
    SELL_GE = "sell_ge"
    DELETE_ITEM = "delete_item"
    DEPOSIT_BANK = "deposit_bank"
    WITHDRAW_BANK = "withdraw_bank"
    EQUIP = "equip"
    UNEQUIP = "unequip"
    TASK = "task"
    RECYCLING = "recycling"


# Action Cooldown Schema
class CooldownSchema(BaseModel):
    """Cooldown Schema."""

    total_seconds: int
    remaining_seconds: int
    expiration: str
    reason: CooldownReasonEnum


# Drop Schema
class DropSchema(BaseModel):
    """Drop Schema."""

    code: str
    quantity: int


# Skill Infos Schema
class SkillInfoSchema(BaseModel):
    """Skill Infos Schema."""

    xp: int
    items: List[DropSchema]


# ---------------------------------------------------------
# MOVE
# ---------------------------------------------------------


# Destination Schema
class MapSchema(BaseModel):
    """Destination Schema."""

    name: str
    x: int
    y: int
    content: Optional[MapContentSchema] = None


# Action Move Schema
class CharacterMovementDataSchema(BaseModel):
    """Action Move Schema."""

    cooldown: CooldownSchema
    destination: MapSchema
    character: CharacterSchema


# Action Move Response Schema
class CharacterMovementDataResponseSchema(BaseModel):
    """Action Move Response Schema."""

    data: CharacterMovementDataSchema


# ---------------------------------------------------------
# EQUIP ITEM
# ---------------------------------------------------------


# Slot Enum
class SlotEnum(str, Enum):
    """Slot Enum."""

    WEAPON = "weapon"
    SHIELD = "shield"
    HELMET = "helmet"
    BODY_ARMOR = "body_armor"
    LEG_ARMOR = "leg_armor"
    BOOTS = "boots"
    RING1 = "ring1"
    RING2 = "ring2"
    AMULET = "amulet"
    ARTIFACT1 = "artifact1"
    ARTIFACT2 = "artifact2"
    ARTIFACT3 = "artifact3"
    CONSUMABLE1 = "consumable1"
    CONSUMABLE2 = "consumable2"


# Item Schema
class EffectSchema(BaseModel):
    """Effect Schema."""

    name: str
    value: int


# Simple Item Schema
class SimpleItemSchema(BaseModel):
    """Simple Item Schema."""

    code: str
    quantity: int


# Craft Schema
class CraftSchema(BaseModel):
    """Craft Schema."""

    skill: str
    level: int
    items: List[SimpleItemSchema]
    quantity: int


# Item Schema
class ItemSchema(BaseModel):
    """Item Schema."""

    name: str
    code: str
    level: int
    type: str
    subtype: str
    description: str
    effects: List[EffectSchema]
    craft: Optional[CraftSchema]


# Action Equip Item Schema
class EquipRequestSchema(BaseModel):
    """Action Equip Item Schema."""

    cooldown: CooldownSchema
    slot: SlotEnum
    item: ItemSchema
    character: CharacterSchema


# Action Equip Item Response Schema
class EquipRequestResponseSchema(BaseModel):
    """Action Equip Item Response Schema."""

    data: EquipRequestSchema


# ---------------------------------------------------------
# FIGHT
# ---------------------------------------------------------


# Fight Result Enum
class FightResultEnum(str, Enum):
    """Fight Result Enum."""

    WIN = "win"
    LOSE = "lose"


# Block Hits Schema
class BlockHitsSchema(BaseModel):
    """Block Hits Schema."""

    fire: int
    earth: int
    water: int
    air: int
    total: int


# Fight Schema
class FightSchema(BaseModel):
    """Fight Schema."""

    xp: int
    gold: int
    drops: List[DropSchema]
    turns: int
    monster_blocked_hits: BlockHitsSchema
    player_blocked_hits: BlockHitsSchema
    logs: List[str]
    result: FightResultEnum


# Action Fight Schema
class CharacterFightDataSchema(BaseModel):
    """Action Fight Schema."""

    cooldown: CooldownSchema
    fight: FightSchema
    character: CharacterSchema


# Action Fight Response Schema
class CharacterFightDataResponseSchema(BaseModel):
    """Action Fight Response Schema."""

    data: CharacterFightDataSchema


# ---------------------------------------------------------
# GATHERING / CRAFTING
# ---------------------------------------------------------


# Action Gathering Schema
class SkillDataSchema(BaseModel):
    """Action Gathering Schema."""

    cooldown: CooldownSchema
    details: SkillInfoSchema
    character: CharacterSchema


# Action Gathering Response Schema
class SkillDataResponseSchema(BaseModel):
    """Action Gathering Response Schema."""

    data: SkillDataSchema


# ---------------------------------------------------------
# BANK ITEM
# ---------------------------------------------------------


# Bank Item Schema
class BankItemSchema(BaseModel):
    """Bank Item Response Schema."""

    cooldown: CooldownSchema
    item: ItemSchema
    bank: List[SimpleItemSchema]
    character: CharacterSchema


# Bank Item Response Schema
class BankItemResponseSchema(BaseModel):
    """Bank Item Response Schema."""

    data: BankItemSchema


class ListBankItemsResponseSchema(BaseModel):
    """List Bank Items Response Schema."""

    data: List[SimpleItemSchema]
    total: int
    page: int
    size: int
    pages: int


# ---------------------------------------------------------
# BANK GOLD
# ---------------------------------------------------------


# Gold Schema
class GoldSchema(BaseModel):
    """Gold Schema."""

    quantity: int


# Gold Transaction Schema
class GoldTransactionSchema(BaseModel):
    """Gold Transaction Schema."""

    cooldown: CooldownSchema
    item: ItemSchema
    bank: GoldSchema
    character: CharacterSchema


# Gold Transaction Response Schema
class GoldTransactionResponseSchema(BaseModel):
    """Gold Transaction Response Schema."""

    data: GoldTransactionSchema


class ListBankGoldsResponseSchema(BaseModel):
    """List Bank Golds Response Schema."""

    data: GoldSchema


# ---------------------------------------------------------
# RECYCLING
# ---------------------------------------------------------


# Recycling Items Schema
class RecyclingItemsSchema(BaseModel):
    """Recycling Items Schema."""

    items: List[DropSchema]


# Recycling Data Schema
class RecyclingDataSchema(BaseModel):
    """Recycling Data Schema."""

    cooldown: CooldownSchema
    details: RecyclingItemsSchema
    character: CharacterSchema


# Recycling Data Response Schema
class RecyclingDataResponseSchema(BaseModel):
    """Recycling Data Response Schema."""

    data: RecyclingDataSchema


# ---------------------------------------------------------
# GRAND EXCHANGE
# ---------------------------------------------------------


# GE Transaction Schema
class GETransactionSchema(BaseModel):
    """GE Transaction Schema."""

    code: str
    quantity: int
    price: int
    total_price: int


# GE Transaction List Schema
class GETransactionListSchema(BaseModel):
    """GE Transaction List Schema."""

    cooldown: CooldownSchema
    transaction: GETransactionSchema
    character: CharacterSchema


# GE Transaction Response Schema
class GETransactionResponseSchema(BaseModel):
    """GE Transaction Response Schema."""

    data: GETransactionListSchema


# ---------------------------------------------------------
# TASK - NEW
# ---------------------------------------------------------


# Task Type Enum
class TaskTypeEnum(str, Enum):
    """Task Type Enum."""

    MONSTERS = "monsters"


# Task Schema
class TaskSchema(BaseModel):
    """Task Schema."""

    code: str
    type: TaskTypeEnum
    total: int


# Task Data Schema
class TaskDataSchema(BaseModel):
    """Task Data Schema."""

    cooldown: CooldownSchema
    task: TaskSchema
    character: CharacterSchema


# Task Data Response Schema
class TaskDataResponseSchema(BaseModel):
    """Task Data Response Schema."""

    data: TaskDataSchema


# ---------------------------------------------------------
# TASK - REWARD
# ---------------------------------------------------------


# Task Reward Schema
class TaskRewardSchema(BaseModel):
    """Task Reward Schema."""

    code: str
    quantity: int


# Task Reward Data Schema
class TaskRewardDataSchema(BaseModel):
    """Task Reward Data Schema."""

    cooldown: CooldownSchema
    reward: TaskRewardSchema
    character: CharacterSchema


# Task Reward Data Response Schema
class TaskRewardDataResponseSchema(BaseModel):
    """Task Reward Data Response Schema."""

    data: TaskRewardDataSchema


# ---------------------------------------------------------
# DELETE ITEM
# ---------------------------------------------------------


# Delete Item Schema
class DeleteItemSchema(BaseModel):
    """Delete Item Schema."""

    cooldown: CooldownSchema
    task: SimpleItemSchema
    character: CharacterSchema


# Delete Item Response Schema
class DeleteItemResponseSchema(BaseModel):
    """Delete Item Response Schema."""

    data: DeleteItemSchema


# ---------------------------------------------------------
# LOGS
# ---------------------------------------------------------


# Logs Schema
class LogsSchema(BaseModel):
    """Logs Schema."""

    character: str
    account: str
    type: str
    description: str
    content: Any
    cooldown: int
    cooldown_expiration: str
    created_at: str


# Logs Response Schema
class LogsResponseSchema(BaseModel):
    """Logs Response Schema."""

    data: List[LogsSchema]
    total: int
    page: int
    size: int
    pages: int


# ---------------------------------------------------------
# CHARACTERS
# ---------------------------------------------------------


# Characters Response Schema
class CharactersResponseSchema(BaseModel):
    """Characters Response Schema."""

    data: List[CharacterSchema]


# ---------------------------------------------------------
# PASSWORD
# ---------------------------------------------------------
class ChangePasswordResponseSchema(BaseModel):
    """ChangePasswordResponseSchema."""

    message: str
