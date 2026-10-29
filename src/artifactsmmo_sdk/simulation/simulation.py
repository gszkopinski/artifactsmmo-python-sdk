"""Simulation."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.simulation import (
    CombatSimulationResponseSchema,
    FakeCharacterSchema,
)


class Simulation(BaseModule):
    """Simulation."""

    def fight_simulation(
        self,
        characters: Annotated[
            list[FakeCharacterSchema],
            Field(description="List of fake characters (1-3)."),
        ],
        monster: Annotated[
            str,
            Field(
                description="Monster code to fight against.", pattern="^[a-zA-Z0-9_-]+$"
            ),
        ],
        iterations: Annotated[
            int,
            Field(description="Number of combat iterations to simulate.", ge=1, le=100),
        ],
    ) -> tuple[str, CombatSimulationResponseSchema | None]:
        """Simulate combat with fake characters against a monster multiple times.
        Member or founder account required."""
        return self._request(
            "POST",
            "/simulation/fight",
            CombatSimulationResponseSchema,
            "Combat simulation completed successfully.",
            {
                404: "Monster or item not found.",
                451: "Access denied, you must be a member to do that.",
                486: "Only boss monsters can be fought by multiple characters.",
            },
            json={
                "characters": characters,
                "monster": monster,
                "iterations": iterations,
            },
        )
