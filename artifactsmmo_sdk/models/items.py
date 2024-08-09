"""Items Schemas."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from .actions import ItemSchema


# ---------------------------------------------------------
# GET ITEM
# ---------------------------------------------------------


# Item Content Schema
class GEItemSchema(BaseModel):
    """Item Content Schema."""

    code: str
    stock: int
    sell_price: int
    buy_price: int


# Single Item Schema
class SingleItemSchema(BaseModel):
    """Single Item Schema."""

    item: ItemSchema
    ge: Optional[GEItemSchema] = None


# Single Item Response Schema
class SingleItemResponseSchema(BaseModel):
    """Single Item Response Schema."""

    data: SingleItemSchema


# ---------------------------------------------------------
# GET ALL ITEMS
# ---------------------------------------------------------


class CraftSkillEnum(str, Enum):
    """Craft Skill Enum."""

    WEAPONCRAFTING = "weaponcrafting"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    COOKING = "cooking"
    WOODCUTTING = "woodcutting"
    MINING = "mining"


# Type Item Enum
class TypeItemEnum(str, Enum):
    """Type Item Enum."""

    WEAPON = "weapon"
    SHIELD = "shield"
    HELMET = "helmet"
    BODY_ARMOR = "body_armor"
    LEG_ARMOR = "leg_armor"
    BOOTS = "boots"
    RING = "ring"
    AMULET = "amulet"
    CONSUMABLE = "consumable"


class ListItemsResponseSchema(BaseModel):
    """List Items Response Schema."""

    data: List[ItemSchema]
    total: int
    page: int
    size: int
    pages: int
