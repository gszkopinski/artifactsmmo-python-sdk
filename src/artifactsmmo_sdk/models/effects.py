"""Effects schemas."""

from enum import Enum

from pydantic import BaseModel


class EffectSubtype(str, Enum):
    """EffectSubtype."""

    STAT = "stat"
    OTHER = "other"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"
    SPECIAL = "special"
    GATHERING = "gathering"
    TELEPORT = "teleport"
    GOLD = "gold"


class EffectType(str, Enum):
    """EffectType."""

    EQUIPMENT = "equipment"
    CONSUMABLE = "consumable"
    COMBAT = "combat"


class EffectSchema(BaseModel):
    """EffectSchema"""

    name: str
    code: str
    description: str
    type: EffectType
    subtype: EffectSubtype


class EffectResponseSchema(BaseModel):
    """EffectResponseSchema"""

    data: EffectSchema


class StaticDataPage_EffectSchema_(BaseModel):
    """StaticDataPage[EffectSchema]"""

    data: list[EffectSchema]
    total: int
    page: int
    size: int
    pages: int
