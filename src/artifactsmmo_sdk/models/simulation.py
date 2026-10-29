"""Simulation schemas."""

from typing import Any

from pydantic import BaseModel


class CombatResultSchema(BaseModel):
    """CombatResultSchema"""

    result: str
    turns: int
    logs: list[str]
    character_results: list[dict[str, Any]]


class CombatSimulationDataSchema(BaseModel):
    """CombatSimulationDataSchema"""

    results: list[CombatResultSchema]
    wins: int
    losses: int
    winrate: float


class CombatSimulationResponseSchema(BaseModel):
    """CombatSimulationResponseSchema"""

    data: CombatSimulationDataSchema


class FakeCharacterSchema(BaseModel):
    """FakeCharacterSchema"""

    level: int
    weapon_slot: str | None = None
    rune_slot: str | None = None
    shield_slot: str | None = None
    helmet_slot: str | None = None
    body_armor_slot: str | None = None
    leg_armor_slot: str | None = None
    boots_slot: str | None = None
    ring1_slot: str | None = None
    ring2_slot: str | None = None
    amulet_slot: str | None = None
    artifact1_slot: str | None = None
    artifact2_slot: str | None = None
    artifact3_slot: str | None = None
    utility1_slot: str | None = None
    utility1_slot_quantity: int | None = None
    utility2_slot: str | None = None
    utility2_slot_quantity: int | None = None
