"""Actions."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.actions import (
    CharacterMovementResponseSchema,
    CharacterRestResponseSchema,
    CharacterTransitionResponseSchema,
)


class Actions(BaseModule):
    """Actions."""

    def move(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        x: Annotated[
            int | None, Field(description="The x coordinate of the destination.")
        ] = None,
        y: Annotated[
            int | None, Field(description="The y coordinate of the destination.")
        ] = None,
        map_id: Annotated[
            int | None, Field(description="The map ID of the destination.")
        ] = None,
    ) -> tuple[str, CharacterMovementResponseSchema | None]:
        """Moves a character on the map using either the map's ID or X and Y position.
        Provide either 'map_id' or both 'x' and 'y' coordinates in the request body."""
        return self._request(
            "POST",
            f"/my/{name}/action/move",
            CharacterMovementResponseSchema,
            "The character has moved successfully.",
            {
                404: "Map not found.",
                490: "The character is already at the destination.",
                496: "Conditions not met.",
                595: "No path available to the destination map.",
                596: "The map is blocked and cannot be accessed.",
            },
            json={
                "x": x,
                "y": y,
                "map_id": map_id,
            },
        )

    def transition(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, CharacterTransitionResponseSchema | None]:
        """Execute a transition from the current map to another layer.
        The character must be on a map that has a transition available."""
        return self._request(
            "POST",
            f"/my/{name}/action/transition",
            CharacterTransitionResponseSchema,
            "The character has transitioned successfully.",
            {
                404: "Transition not found.",
                492: "Insufficient gold for this transition.",
                496: "Conditions not met.",
            },
        )

    def rest(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, CharacterRestResponseSchema | None]:
        """Recovers hit points by resting. (1 second per 5 HP, minimum 3 seconds)"""
        return self._request(
            "POST",
            f"/my/{name}/action/rest",
            CharacterRestResponseSchema,
            "The character has rested successfully.",
        )
