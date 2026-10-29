"""Actions schemas."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from .common import (
    CharacterSchema,
    ItemSchema,
    MapSchema,
    SimpleItemSchema,
    TransitionSchema,
)


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


class BankExtensionSchema(BaseModel):
    """BankExtensionSchema"""

    price: int


class CooldownSchema(BaseModel):
    """CooldownSchema"""

    total_seconds: int
    remaining_seconds: int
    started_at: datetime
    expiration: datetime
    reason: ActionType


class BankExtensionTransactionSchema(BaseModel):
    """BankExtensionTransactionSchema"""

    cooldown: CooldownSchema
    transaction: BankExtensionSchema
    character: CharacterSchema


class BankExtensionTransactionResponseSchema(BaseModel):
    """BankExtensionTransactionResponseSchema"""

    data: BankExtensionTransactionSchema


class GoldSchema(BaseModel):
    """GoldSchema"""

    quantity: int


class BankGoldTransactionSchema(BaseModel):
    """BankGoldTransactionSchema"""

    cooldown: CooldownSchema
    bank: GoldSchema
    character: CharacterSchema


class BankGoldTransactionResponseSchema(BaseModel):
    """BankGoldTransactionResponseSchema"""

    data: BankGoldTransactionSchema


class BankItemTransactionSchema(BaseModel):
    """BankItemTransactionSchema"""

    cooldown: CooldownSchema
    items: list[SimpleItemSchema]
    bank: list[SimpleItemSchema]
    character: CharacterSchema


class BankItemTransactionResponseSchema(BaseModel):
    """BankItemTransactionResponseSchema"""

    data: BankItemTransactionSchema


class DropSchema(BaseModel):
    """DropSchema"""

    code: str
    quantity: int


class CharacterMultiFightResultSchema(BaseModel):
    """CharacterMultiFightResultSchema"""

    character_name: str
    xp: int
    gold: int
    drops: list[DropSchema]
    final_hp: int


class FightResult(str, Enum):
    """FightResult."""

    WIN = "win"
    LOSS = "loss"


class CharacterFightSchema(BaseModel):
    """CharacterFightSchema"""

    result: FightResult
    turns: int
    opponent: str
    logs: list[str]
    characters: list[CharacterMultiFightResultSchema]


class CharacterFightDataSchema(BaseModel):
    """CharacterFightDataSchema"""

    cooldown: CooldownSchema
    fight: CharacterFightSchema
    characters: list[CharacterSchema]


class CharacterFightResponseSchema(BaseModel):
    """CharacterFightResponseSchema"""

    data: CharacterFightDataSchema


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


class ItemSlot(str, Enum):
    """ItemSlot."""

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
    UTILITY1 = "utility1"
    UTILITY2 = "utility2"
    BAG = "bag"
    RUNE = "rune"


class EquipSchema(BaseModel):
    """EquipSchema"""

    code: str
    slot: ItemSlot
    quantity: int | None = None


class EquipmentItemSchema(BaseModel):
    """EquipmentItemSchema"""

    slot: ItemSlot
    item: ItemSchema


class EquipmentTransactionSchema(BaseModel):
    """EquipmentTransactionSchema"""

    cooldown: CooldownSchema
    items: list[EquipmentItemSchema]
    character: CharacterSchema


class EquipmentResponseSchema(BaseModel):
    """EquipmentResponseSchema"""

    data: EquipmentTransactionSchema


class GETransactionSchema(BaseModel):
    """GETransactionSchema"""

    id: str
    code: str
    quantity: int
    price: int
    total_price: int


class GETransactionListSchema(BaseModel):
    """GETransactionListSchema"""

    cooldown: CooldownSchema
    order: GETransactionSchema
    character: CharacterSchema


class GETransactionResponseSchema(BaseModel):
    """GETransactionResponseSchema"""

    data: GETransactionListSchema


class NpcItemTransactionSchema(BaseModel):
    """NpcItemTransactionSchema"""

    code: str
    quantity: int
    currency: str
    price: int
    total_price: int


class NpcMerchantTransactionSchema(BaseModel):
    """NpcMerchantTransactionSchema"""

    cooldown: CooldownSchema
    transaction: NpcItemTransactionSchema
    character: CharacterSchema


class NpcMerchantTransactionResponseSchema(BaseModel):
    """NpcMerchantTransactionResponseSchema"""

    data: NpcMerchantTransactionSchema


class RecyclingItemsSchema(BaseModel):
    """RecyclingItemsSchema"""

    items: list[DropSchema]
    enhanced: bool | None = None
    gold: int | None = None


class RecyclingDataSchema(BaseModel):
    """RecyclingDataSchema"""

    cooldown: CooldownSchema
    details: RecyclingItemsSchema
    character: CharacterSchema


class RecyclingResponseSchema(BaseModel):
    """RecyclingResponseSchema"""

    data: RecyclingDataSchema


class SkillInfoSchema(BaseModel):
    """SkillInfoSchema"""

    xp: int
    items: list[DropSchema]


class SkillDataSchema(BaseModel):
    """SkillDataSchema"""

    cooldown: CooldownSchema
    details: SkillInfoSchema
    character: CharacterSchema


class SkillResponseSchema(BaseModel):
    """SkillResponseSchema"""

    data: SkillDataSchema


class UnequipSchema(BaseModel):
    """UnequipSchema"""

    slot: ItemSlot
    quantity: int | None = None


class UseItemSchema(BaseModel):
    """UseItemSchema"""

    cooldown: CooldownSchema
    item: ItemSchema
    character: CharacterSchema


class UseItemResponseSchema(BaseModel):
    """UseItemResponseSchema"""

    data: UseItemSchema
