"""Actions."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.actions import (
    BankItemResponseSchema,
    CharacterFightDataResponseSchema,
    CharacterMovementDataResponseSchema,
    CharacterRestDataResponseSchema,
    CharactersResponseSchema,
    CharacterTransitionDataResponseSchema,
    DeleteItemResponseSchema,
    EquipRequestResponseSchema,
    GETransactionResponseSchema,
    GoldTransactionResponseSchema,
    LogsResponseSchema,
    RecyclingDataResponseSchema,
    SkillDataResponseSchema,
    SlotEnum,
    TaskDataResponseSchema,
    TaskRewardDataResponseSchema,
    UseItemResponseSchema,
)


class Actions(BaseModule):
    """Characters."""

    def move(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        x: Annotated[int, Field(description="The x coordinate of the destination.")],
        y: Annotated[int, Field(description="The y coordinate of the destination.")],
        map_id: Annotated[int, Field(description="The map ID of the destination.")] = 0,
    ) -> tuple[str, CharacterMovementDataResponseSchema | None]:
        """Moves a character on the map using either the map's ID or X and Y position.
        Provide either 'map_id' or both 'x' and 'y' coordinates in the request body."""
        return self._request(
            "POST",
            f"/my/{name}/action/move",
            CharacterMovementDataResponseSchema,
            "The character has moved successfully.",
            {
                404: "Map not found.",
                490: "The character is already at the destination.",
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
    ) -> tuple[str, CharacterTransitionDataResponseSchema | None]:
        """Execute a transition from the current map to another layer.
        The character must be on a map that has a transition available."""
        return self._request(
            "POST",
            f"/my/{name}/action/transition",
            CharacterTransitionDataResponseSchema,
            "The character has transitioned successfully.",
            {
                404: "Transition not found.",
                597: "No transition available on this map.",
            },
        )

    def rest(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, CharacterRestDataResponseSchema | None]:
        """Recovers hit points by resting. (1 second per 5 HP, minimum 3 seconds)."""
        return self._request(
            "POST",
            f"/my/{name}/action/rest",
            CharacterRestDataResponseSchema,
            "The character has rested successfully.",
            {
                486: "An action is already in progress by your character.",
            },
        )

    def equip_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        slot: Annotated[SlotEnum, Field(description="Item slot.")],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, le=100, default=1)
        ] = 1,
    ) -> tuple[str, EquipRequestResponseSchema | None]:
        """Equip an item on your character."""
        return self._request(
            "POST",
            f"/my/{name}/action/equip",
            EquipRequestResponseSchema,
            "The item has been successfully equipped on your character.",
            {
                404: "Item not found.",
                478: "Missing item or insufficient quantity in your inventory.",
                483: "The character does not have enough HP to unequip this item.",
                484: "The character cannot equip more than 100 utilities in the same slot.",
                485: "This item is already equipped.",
                486: "Character is locked. Action is already in progress.",
                491: "Slot is not empty.",
                496: "Character level is insufficient.",
                497: "Character's inventory is full.",
                499: "The character is in cooldown.",
            },
            json={
                "code": code,
                "slot": slot,
                "quantity": quantity,
            },
        )

    def unequip_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        slot: Annotated[SlotEnum, Field(description="Item slot.")],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, le=100, default=1)
        ] = 1,
    ) -> tuple[str, EquipRequestResponseSchema | None]:
        """Unequip an item on your character."""
        return self._request(
            "POST",
            f"/my/{name}/action/unequip",
            EquipRequestResponseSchema,
            "The item has been successfully unequipped and added in his inventory.",
            {
                404: "Item not found.",
                478: "Missing required item(s).",
                483: "The character does not have enough HP to unequip this item.",
                491: "Slot is empty.",
                497: "Character's inventory is full.",
                499: "The character is in cooldown.",
            },
            json={
                "slot": slot,
                "quantity": quantity,
            },
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
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, le=100, default=1)
        ] = 1,
    ) -> tuple[str, UseItemResponseSchema | None]:
        """Use an item from your character's inventory."""
        return self._request(
            "POST",
            f"/my/{name}/action/use",
            UseItemResponseSchema,
            "The item has been successfully used by your character.",
            {
                404: "Item not found.",
                478: "Missing item or insufficient quantity in your inventory.",
                486: "Character is locked. Action is already in progress.",
                499: "The character is in cooldown.",
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
            Field(description="List of participant character names.", le=2),
        ] = None,
    ) -> tuple[str, CharacterFightDataResponseSchema | None]:
        """Start a fight against a monster on the character's map.
        Add participants for multi-character fights (up to 3 characters, only for boss)."""
        return self._request(
            "POST",
            f"/my/{name}/action/fight",
            CharacterFightDataResponseSchema,
            "The fight ended successfully.",
            {
                486: "Character is locked. Action is already in progress.",
                497: "Character inventory is full.",
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
    ) -> tuple[str, SkillDataResponseSchema | None]:
        """Harvest a resource on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/gathering",
            SkillDataResponseSchema,
            "The resource has been successfully gathered.",
            {
                404: "Item not found.",
                486: "Character is locked. Action is already in progress.",
                493: "Not skill level required.",
                497: "Character inventory is full.",
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
            int, Field(description="Quantity of items to craft.", ge=1, default=1)
        ] = 1,
    ) -> tuple[str, SkillDataResponseSchema | None]:
        """Crafting an item. The character must be on a map with a workshop."""
        return self._request(
            "POST",
            f"/my/{name}/action/crafting",
            SkillDataResponseSchema,
            "The item was successfully crafted.",
            {
                404: "Craft not found.",
                478: "Missing item or insufficient quantity in your inventory.",
                486: "Character is locked. Action is already in progress.",
                493: "Not skill level required.",
                497: "Character inventory is full.",
                598: "Workshop not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )

    def deposit_bank(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, default=1)
        ] = 1,
    ) -> tuple[str, BankItemResponseSchema | None]:
        """Deposit an item in a bank on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/deposit",
            BankItemResponseSchema,
            "Item successfully deposited in your bank.",
            {
                404: "Item not found.",
                478: "Missing item or insufficient quantity in your inventory.",
                486: "Character is locked. Action is already in progress.",
                598: "Bank not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )

    def deposit_bank_gold(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, default=1)
        ] = 1,
    ) -> tuple[str, GoldTransactionResponseSchema | None]:
        """Deposit golds in a bank on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/deposit/gold",
            GoldTransactionResponseSchema,
            "Golds successfully deposited in your bank.",
            {
                478: "Missing item or insufficient quantity in your inventory.",
                486: "Character is locked. Action is already in progress.",
                492: "Insufficient golds on your character.",
                598: "Bank not found on this map.",
            },
            json={
                "quantity": quantity,
            },
        )

    def recycling(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[
            int, Field(description="Quantity of items to recycle.", ge=1, default=1)
        ] = 1,
    ) -> tuple[str, RecyclingDataResponseSchema | None]:
        """Recyling an item. The character must be on a map with a workshop (only for equipments and weapons)."""
        return self._request(
            "POST",
            f"/my/{name}/action/recycling",
            RecyclingDataResponseSchema,
            "The items were successfully recycled.",
            {
                404: "Item not found.",
                473: "Quantity of items to recycle.",
                478: "Missing item or insufficient quantity in your inventory.",
                486: "Character is locked. Action is already in progress.",
                493: "Not skill level required.",
                497: "Character inventory is full.",
                598: "Workshop not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )

    def withdraw_bank(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, default=1)
        ] = 1,
    ) -> tuple[str, BankItemResponseSchema | None]:
        """Take an item from your bank and put it in the character's inventory."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/withdraw",
            BankItemResponseSchema,
            "Item successfully withdraw from your bank.",
            {
                404: "Item not found.",
                478: "Missing item or insufficient quantity in your inventory.",
                486: "Character is locked. Action is already in progress.",
                497: "Character inventory is full.",
                598: "Bank not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )

    def withdraw_bank_gold(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, default=1)
        ] = 1,
    ) -> tuple[str, GoldTransactionResponseSchema | None]:
        """Withdraw gold from your bank."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/withdraw/gold",
            GoldTransactionResponseSchema,
            "Golds successfully withdraw from your bank.",
            {
                460: "Insufficient golds in your bank.",
                486: "Character is locked. Action is already in progress.",
                598: "Bank not found on this map.",
            },
            json={
                "quantity": quantity,
            },
        )

    def ge_buy_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        price: Annotated[int, Field(description="Item quantity.", ge=1)],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, le=50, default=1)
        ] = 1,
    ) -> tuple[str, GETransactionResponseSchema | None]:
        """Buy an item at the Grand Exchange on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/ge/buy",
            GETransactionResponseSchema,
            "Item successfully buy from the Grand Exchange.",
            {
                480: "No stock for this item.",
                482: "No item at this price.",
                486: "Character is locked. Action is already in progress.",
                492: "Insufficient golds on your character.",
                497: "Character inventory is full.",
                598: "Grand Exchange not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
                "price": price,
            },
        )

    def ge_sell_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        price: Annotated[int, Field(description="Item quantity.", ge=1)],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, le=50, default=1)
        ] = 1,
    ) -> tuple[str, GETransactionResponseSchema | None]:
        """Sell an item at the Grand Exchange on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/ge/sell",
            GETransactionResponseSchema,
            "Item successfully sell at the Grand Exchange.",
            {
                404: "Item not found.",
                478: "Missing item or insufficient quantity in your inventory.",
                482: "No item at this price.",
                486: "Character is locked. Action is already in progress.",
                598: "Grand Exchange not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
                "price": price,
            },
        )

    def accept_new_task(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, TaskDataResponseSchema | None]:
        """Accept a new task."""
        return self._request(
            "POST",
            f"/my/{name}/action/task/new",
            TaskDataResponseSchema,
            "New task successfully accepted.",
            {
                486: "Character is locked. Action is already in progress.",
                489: "Character already has a task.",
                598: "Tasks Master not found on this map.",
            },
        )

    def complete_task(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, TaskRewardDataResponseSchema | None]:
        """Complete a task."""
        return self._request(
            "POST",
            f"/my/{name}/action/task/complete",
            TaskRewardDataResponseSchema,
            "The task has been successfully completed.",
            {
                486: "Character is locked. Action is already in progress.",
                487: "Character has no task.",
                488: "Character has not completed the task.",
                497: "Character inventory is full.",
                598: "Tasks Master not found on this map.",
            },
        )

    def task_exchange(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, TaskRewardDataResponseSchema | None]:
        """Exchange 3 tasks coins for a random reward. Rewards are exclusive resources for crafting items."""
        return self._request(
            "POST",
            f"/my/{name}/action/task/exchange",
            TaskRewardDataResponseSchema,
            "The tasks coins have been successfully exchanged.",
            {
                478: "Missing item or insufficient quantity in your inventory.",
                486: "Character is locked. Action is already in progress.",
                497: "Character inventory is full..",
                598: "Tasks Master not found on this map.",
            },
        )

    def delete_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[
            int, Field(description="Item quantity.", ge=1, default=1)
        ] = 1,
    ) -> tuple[str, DeleteItemResponseSchema | None]:
        """Delete an item from your character's inventory.."""
        return self._request(
            "POST",
            f"/my/{name}/action/delete",
            DeleteItemResponseSchema,
            "Item successfully deleted from your character.",
            {
                478: "Missing item or insufficient quantity in your inventory.",
                486: "Character is locked. Action is already in progress.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )

    def get_all_character_logs(
        self,
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, LogsResponseSchema | None]:
        """Get all character logs."""
        return self._request(
            "GET",
            "/my/logs",
            LogsResponseSchema,
            "Successfully fetched logs.",
            {
                404: "Logs not found.",
            },
            params={
                "page": page,
                "size": size,
            },
        )

    def get_my_characters(
        self,
    ) -> tuple[str, CharactersResponseSchema | None]:
        """List of your characters."""
        return self._request(
            "GET",
            "/my/characters",
            CharactersResponseSchema,
            "Successfully fetched characters.",
            {
                404: "Character not found.",
            },
        )
