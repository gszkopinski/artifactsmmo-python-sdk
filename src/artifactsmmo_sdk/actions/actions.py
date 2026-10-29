"""Actions."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.actions import (
    CharacterFightResponseSchema,
    CharacterMovementResponseSchema,
    CharacterRestResponseSchema,
    CharacterTransitionResponseSchema,
    EquipmentResponseSchema,
    EquipSchema,
    SkillResponseSchema,
    UnequipSchema,
    UseItemResponseSchema,
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

    def equip_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        items: Annotated[
            list[EquipSchema], Field(description="List of items to equip.")
        ],
    ) -> tuple[str, EquipmentResponseSchema | None]:
        """Equip multiple items on your character.
        The cooldown will be 3 seconds multiplied by the number of different items equipped."""
        return self._request(
            "POST",
            f"/my/{name}/action/equip",
            EquipmentResponseSchema,
            "The item has been successfully equipped on your character.",
            {
                404: "Item not found.",
                483: "The character does not have enough HP to unequip this item.",
                484: "The character cannot equip more than 100 utilities in the same slot.",
                485: "This item is already equipped.",
                491: "The equipment slot is not empty.",
                496: "Conditions not met.",
            },
            json=[item.model_dump(mode="json", exclude_none=True) for item in items],
        )

    def unequip_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        items: Annotated[
            list[UnequipSchema], Field(description="List of items to unequip.")
        ],
    ) -> tuple[str, EquipmentResponseSchema | None]:
        """Unequip multiple items on your character.
        The cooldown will be 3 seconds multiplied by the number of different items unequipped."""
        return self._request(
            "POST",
            f"/my/{name}/action/unequip",
            EquipmentResponseSchema,
            "The item has been successfully unequipped and added in their inventory.",
            {
                404: "Item not found.",
                483: "The character does not have enough HP to unequip this item.",
                491: "The equipment slot is empty.",
            },
            json=[item.model_dump(mode="json", exclude_none=True) for item in items],
        )

    def use_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1)],
    ) -> tuple[str, UseItemResponseSchema | None]:
        """Use an item as a consumable."""
        return self._request(
            "POST",
            f"/my/{name}/action/use",
            UseItemResponseSchema,
            "The item has been successfully used.",
            {
                404: "Item not found.",
                476: "This item is not a consumable.",
                496: "Conditions not met.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )

    def fight(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        participants: Annotated[
            list[str] | None,
            Field(
                description="Optional list of additional character names to include in the fight (max 2 additional characters)."
            ),
        ] = None,
    ) -> tuple[str, CharacterFightResponseSchema | None]:
        """Start a fight against a monster on the character's map.
        Add participants for multi-character fights (up to 3 characters, only for boss)."""
        return self._request(
            "POST",
            f"/my/{name}/action/fight",
            CharacterFightResponseSchema,
            "The fight ended successfully.",
            {
                486: "Only boss monsters can be fought by multiple characters.",
                567: "This raid phase is not currently active.",
                598: "Monster not found on this map.",
            },
            json={
                "participants": participants,
            },
        )

    def gathering(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, SkillResponseSchema | None]:
        """Harvest a resource on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/gathering",
            SkillResponseSchema,
            "The resource has been successfully gathered.",
            {
                493: "The character's skill level is too low.",
                598: "Resource not found on this map.",
            },
        )

    def crafting(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Craft code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[
            int | None, Field(description="Quantity of items to craft.", ge=1)
        ] = None,
    ) -> tuple[str, SkillResponseSchema | None]:
        """Craft an item. The character must be on a map with a workshop."""
        return self._request(
            "POST",
            f"/my/{name}/action/crafting",
            SkillResponseSchema,
            "The item was successfully crafted.",
            {
                404: "Craft not found.",
                493: "The character's skill level is too low.",
                598: "Workshop not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )
