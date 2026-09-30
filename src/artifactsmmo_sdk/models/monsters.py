"""Monsters Models."""

from pydantic import BaseModel

from .common import DropRateSchema


class MonsterSchema(BaseModel):
    """Monster Model."""

    name: str
    code: str
    level: int
    hp: int
    attack_fire: int
    attack_earth: int
    attack_water: int
    attack_air: int
    res_fire: int
    res_earth: int
    res_water: int
    res_air: int
    min_gold: int
    max_gold: int
    drops: list[DropRateSchema]


class MonsterResponseSchema(BaseModel):
    """Monster Response Model."""

    data: MonsterSchema


class ListMonsterResponseSchema(BaseModel):
    """List Monster Response Schema."""

    data: list[MonsterSchema]
    total: int
    page: int
    size: int
    pages: int
