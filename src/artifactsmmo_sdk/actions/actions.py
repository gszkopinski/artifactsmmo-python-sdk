"""Actions."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.actions import (
    CharacterMovementResponseSchema,
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
