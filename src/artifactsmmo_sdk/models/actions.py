"""Actions schemas."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from .common import CharacterSchema, MapSchema, TransitionSchema


class ActionType(str, Enum):
    """ActionType."""

    MOVEMENT = "movement"
    FIGHT = "fight"
    RAID_FIGHT = "raid_fight"
    MULTI_FIGHT = "multi_fight"
    CRAFTING = "crafting"
    GATHERING = "gathering"
    BUY_GE = "buy_ge"
    SELL_GE = "sell_ge"
    CREATE_BUY_ORDER_GE = "create_buy_order_ge"
    FILL_BUY_ORDER_GE = "fill_buy_order_ge"
    BUY_NPC = "buy_npc"
    SELL_NPC = "sell_npc"
    CANCEL_GE = "cancel_ge"
    DELETE_ITEM = "delete_item"
    DEPOSIT_ITEM = "deposit_item"
    WITHDRAW_ITEM = "withdraw_item"
    DEPOSIT_GOLD = "deposit_gold"
    WITHDRAW_GOLD = "withdraw_gold"
    EQUIP = "equip"
    UNEQUIP = "unequip"
    TASK = "task"
    RECYCLING = "recycling"
    REST = "rest"
    USE = "use"
    BUY_BANK_EXPANSION = "buy_bank_expansion"
    GIVE_ITEM = "give_item"
    GIVE_GOLD = "give_gold"
    RAID_DEPOSIT = "raid_deposit"
    CHANGE_SKIN = "change_skin"
    RENAME = "rename"
    TRANSITION = "transition"
    CLAIM_ITEM = "claim_item"
    SANDBOX_GIVE_GOLD = "sandbox_give_gold"
    SANDBOX_GIVE_ITEM = "sandbox_give_item"
    SANDBOX_GIVE_XP = "sandbox_give_xp"
    SANDBOX_CLEAR_COOLDOWN = "sandbox_clear_cooldown"
    SANDBOX_TELEPORT = "sandbox_teleport"


class CooldownSchema(BaseModel):
    """CooldownSchema"""

    total_seconds: int
    remaining_seconds: int
    started_at: datetime
    expiration: datetime
    reason: ActionType


class CharacterMovementDataSchema(BaseModel):
    """CharacterMovementDataSchema"""

    cooldown: CooldownSchema
    destination: MapSchema
    path: list[list[int]]
    character: CharacterSchema


class CharacterMovementResponseSchema(BaseModel):
    """CharacterMovementResponseSchema"""

    data: CharacterMovementDataSchema


class CharacterRestDataSchema(BaseModel):
    """CharacterRestDataSchema"""

    cooldown: CooldownSchema
    hp_restored: int
    character: CharacterSchema


class CharacterRestResponseSchema(BaseModel):
    """CharacterRestResponseSchema"""

    data: CharacterRestDataSchema


class CharacterTransitionDataSchema(BaseModel):
    """CharacterTransitionDataSchema"""

    cooldown: CooldownSchema
    destination: MapSchema
    transition: TransitionSchema
    character: CharacterSchema


class CharacterTransitionResponseSchema(BaseModel):
    """CharacterTransitionResponseSchema"""

    data: CharacterTransitionDataSchema
