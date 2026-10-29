"""Monsters schemas."""

from enum import Enum

from pydantic import BaseModel

from .common import DropRateSchema, SimpleEffectSchema


class MonsterType(str, Enum):
    """MonsterType."""

    NORMAL = "normal"
    ELITE = "elite"
    BOSS = "boss"
    RAID_BOSS = "raid_boss"


class MonsterSchema(BaseModel):
    """MonsterSchema"""

    name: str
    code: str
    level: int
    type: MonsterType
    hp: int
    attack_fire: int
    attack_earth: int
    attack_water: int
    attack_air: int
    res_fire: int
    res_earth: int
    res_water: int
    res_air: int
    critical_strike: int
    initiative: int
    effects: list[SimpleEffectSchema] | None = None
    min_gold: int
    max_gold: int
    drops: list[DropRateSchema]


class MonsterResponseSchema(BaseModel):
    """MonsterResponseSchema"""

    data: MonsterSchema


class StaticDataPage_MonsterSchema_(BaseModel):
    """StaticDataPage[MonsterSchema]"""

    data: list[MonsterSchema]
    total: int
    page: int
    size: int
    pages: int
