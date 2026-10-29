"""Actions."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.actions import (
    BankExtensionTransactionResponseSchema,
    BankGoldTransactionResponseSchema,
    BankItemTransactionResponseSchema,
    CharacterFightResponseSchema,
    CharacterMovementResponseSchema,
    CharacterRestResponseSchema,
    CharacterTransitionResponseSchema,
    EquipmentResponseSchema,
    EquipSchema,
    GECreateOrderTransactionResponseSchema,
    GETransactionResponseSchema,
    GiveGoldResponseSchema,
    GiveItemResponseSchema,
    NpcMerchantTransactionResponseSchema,
    RecyclingResponseSchema,
    RewardDataResponseSchema,
    SkillResponseSchema,
    TaskCancelledResponseSchema,
    TaskResponseSchema,
    TaskTradeResponseSchema,
    UnequipSchema,
    UseItemResponseSchema,
)
from ..models.common import (
    SimpleItemSchema,
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

    def deposit_bank_gold(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        quantity: Annotated[int, Field(description="Quantity of gold.", ge=1)],
    ) -> tuple[str, BankGoldTransactionResponseSchema | None]:
        """Deposit gold in a bank on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/deposit/gold",
            BankGoldTransactionResponseSchema,
            "Golds successfully deposited in your bank.",
            {
                461: "Some of your items or your gold in the bank are already part of an ongoing transaction.",
                492: "The character does not have enough gold.",
                598: "Bank not found on this map.",
            },
            json={
                "quantity": quantity,
            },
        )

    def deposit_bank(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        items: Annotated[
            list[SimpleItemSchema],
            Field(description="List of items to deposit in the bank."),
        ],
    ) -> tuple[str, BankItemTransactionResponseSchema | None]:
        """Deposit multiple items in a bank on the character's map.
        The cooldown will be 3 seconds multiplied by the number of different items deposited."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/deposit/item",
            BankItemTransactionResponseSchema,
            "Items successfully deposited in your bank.",
            {
                404: "Item not found.",
                461: "Some of your items or your gold in the bank are already part of an ongoing transaction.",
                462: "Your bank is full.",
                598: "Bank not found on this map.",
            },
            json=[item.model_dump(mode="json", exclude_none=True) for item in items],
        )

    def withdraw_bank(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        items: Annotated[list[SimpleItemSchema], Field(description="")],
    ) -> tuple[str, BankItemTransactionResponseSchema | None]:
        """Take items from your bank and put them in the character's inventory.
        The cooldown will be 3 seconds multiplied by the number of different items withdrawn."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/withdraw/item",
            BankItemTransactionResponseSchema,
            "Items successfully withdrawn from your bank.",
            {
                404: "Item not found.",
                461: "Some of your items or your gold in the bank are already part of an ongoing transaction.",
                598: "Bank not found on this map.",
            },
            json=[item.model_dump(mode="json", exclude_none=True) for item in items],
        )

    def withdraw_bank_gold(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        quantity: Annotated[int, Field(description="Quantity of gold.", ge=1)],
    ) -> tuple[str, BankGoldTransactionResponseSchema | None]:
        """Withdraw gold from your bank."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/withdraw/gold",
            BankGoldTransactionResponseSchema,
            "Golds successfully withdraw from your bank.",
            {
                460: "Insufficient gold in your bank.",
                461: "Some of your items or your gold in the bank are already part of an ongoing transaction.",
                598: "Bank not found on this map.",
            },
            json={
                "quantity": quantity,
            },
        )

    def buy_bank_expansion(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, BankExtensionTransactionResponseSchema | None]:
        """Buy a 20 slots bank expansion."""
        return self._request(
            "POST",
            f"/my/{name}/action/bank/buy_expansion",
            BankExtensionTransactionResponseSchema,
            "Bank expansion successfully bought.",
            {
                492: "The character does not have enough gold.",
                598: "Bank not found on this map.",
            },
        )

    def npc_buy_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[str, Field(description="Item code.")],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1)],
    ) -> tuple[str, NpcMerchantTransactionResponseSchema | None]:
        """Buy an item from an NPC on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/npc/buy",
            NpcMerchantTransactionResponseSchema,
            "Item successfully bought from the NPC.",
            {
                404: "Item not found.",
                441: "This item is not available for purchase.",
                492: "The character does not have enough gold.",
                598: "NPC not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )

    def npc_sell_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[str, Field(description="Item code.")],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1)],
    ) -> tuple[str, NpcMerchantTransactionResponseSchema | None]:
        """Sell an item to an NPC on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/npc/sell",
            NpcMerchantTransactionResponseSchema,
            "Item successfully sold to the NPC.",
            {
                404: "Item not found.",
                441: "This item is not available to be sold.",
                598: "NPC not found on this map.",
            },
            json={
                "code": code,
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
            int | None, Field(description="Quantity of items to recycle.", ge=1)
        ] = None,
        enhanced: Annotated[
            bool | None, Field(description="Whether to use enhanced recycling.")
        ] = None,
    ) -> tuple[str, RecyclingResponseSchema | None]:
        """Recycling an item. The character must be on a map with a workshop (only for equipments and weapons)."""
        return self._request(
            "POST",
            f"/my/{name}/action/recycling",
            RecyclingResponseSchema,
            "The items were successfully recycled.",
            {
                404: "Item not found.",
                473: "This item cannot be recycled.",
                492: "The character does not have enough gold.",
                493: "The character's skill level is too low.",
                598: "Workshop not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
                "enhanced": enhanced,
            },
        )

    def ge_buy_item(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        id: Annotated[str, Field(description="Order id.")],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, le=100)],
    ) -> tuple[str, GETransactionResponseSchema | None]:
        """Buy an item at the Grand Exchange on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/grandexchange/buy",
            GETransactionResponseSchema,
            "Item successfully bought from the Grand Exchange.",
            {
                404: "Order not found.",
                434: "This offer does not contain that many items.",
                435: "You cannot trade with yourself.",
                436: "A transaction is already in progress for this order by another character.",
                492: "The character does not have enough gold.",
                598: "Grand Exchange not found on this map.",
            },
            json={
                "id": id,
                "quantity": quantity,
            },
        )

    def ge_create_sell_order(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, le=100)],
        price: Annotated[
            int, Field(description="Item price per unit.", ge=1, le=1000000000)
        ],
    ) -> tuple[str, GECreateOrderTransactionResponseSchema | None]:
        """Create a sell order at the Grand Exchange on the character's map."""
        return self._request(
            "POST",
            f"/my/{name}/action/grandexchange/create_sell_order",
            GECreateOrderTransactionResponseSchema,
            "The sell order has been successfully created.",
            {
                404: "Item not found.",
                433: "You cannot create more than 100 orders at the same time.",
                437: "This item cannot be sold.",
                598: "Grand Exchange not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
                "price": price,
            },
        )

    def ge_cancel_order(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        id: Annotated[str, Field(description="Order id.")],
    ) -> tuple[str, GETransactionResponseSchema | None]:
        """Cancel an order (sell or buy) at the Grand Exchange on the character's map.

        For sell orders: Items are returned to your inventory.
        For buy orders: Gold is refunded to your character."""
        return self._request(
            "POST",
            f"/my/{name}/action/grandexchange/cancel",
            GETransactionResponseSchema,
            "Your order has been successfully cancelled.",
            {
                404: "Order not found.",
                436: "A transaction is already in progress for this order by another character.",
                438: "You cannot cancel an order that is not yours.",
                598: "Grand Exchange not found on this map.",
            },
            json={
                "id": id,
            },
        )

    def ge_create_buy_order(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1)],
        price: Annotated[
            int, Field(description="Item price per unit.", ge=1, le=1000000000)
        ],
    ) -> tuple[str, GECreateOrderTransactionResponseSchema | None]:
        """Create a buy order at the Grand Exchange on the character's map.

        The total gold (price * quantity) is locked when creating the order.
        Other players can then sell items to fulfill your order.
        Items will be delivered to your pending items when the order is filled."""
        return self._request(
            "POST",
            f"/my/{name}/action/grandexchange/create_buy_order",
            GECreateOrderTransactionResponseSchema,
            "The buy order has been successfully created.",
            {
                404: "Item not found.",
                433: "You cannot create more than 100 orders at the same time.",
                437: "This item cannot be sold.",
                492: "The character does not have enough gold.",
                598: "Grand Exchange not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
                "price": price,
            },
        )

    def ge_fill(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        id: Annotated[str, Field(description="Buy order id.")],
        quantity: Annotated[
            int, Field(description="Item quantity to sell.", ge=1, le=100)
        ],
    ) -> tuple[str, GETransactionResponseSchema | None]:
        """Sell items to an existing buy order at the Grand Exchange on the character's map.

        You will receive the gold immediately.
        The buyer will receive the items in their pending items."""
        return self._request(
            "POST",
            f"/my/{name}/action/grandexchange/fill",
            GETransactionResponseSchema,
            "Successfully sold items to the buy order.",
            {
                404: "Buy order not found.",
                434: "This offer does not contain that many items.",
                435: "You cannot trade with yourself.",
                436: "A transaction is already in progress for this order by another character.",
                598: "Grand Exchange not found on this map.",
            },
            json={
                "id": id,
                "quantity": quantity,
            },
        )

    def complete_task(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, RewardDataResponseSchema | None]:
        """Complete a task."""
        return self._request(
            "POST",
            f"/my/{name}/action/task/complete",
            RewardDataResponseSchema,
            "The task has been successfully completed.",
            {
                487: "The character has no task assigned.",
                488: "The character has not completed the task.",
                598: "Tasks Master not found on this map.",
            },
        )

    def task_exchange(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, RewardDataResponseSchema | None]:
        """Exchange 6 tasks coins for a random reward. Rewards are exclusive items or resources."""
        return self._request(
            "POST",
            f"/my/{name}/action/task/exchange",
            RewardDataResponseSchema,
            "The tasks coins have been successfully exchanged.",
            {
                598: "Tasks Master not found on this map.",
            },
        )

    def accept_new_task(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, TaskResponseSchema | None]:
        """Accepting a new task."""
        return self._request(
            "POST",
            f"/my/{name}/action/task/new",
            TaskResponseSchema,
            "New task successfully accepted.",
            {
                489: "The character already has an assigned task.",
                598: "Tasks Master not found on this map.",
            },
        )

    def task_trade(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        code: Annotated[
            str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1)],
    ) -> tuple[str, TaskTradeResponseSchema | None]:
        """Trading items with a Tasks Master."""
        return self._request(
            "POST",
            f"/my/{name}/action/task/trade",
            TaskTradeResponseSchema,
            "You have successfully trade items to a Tasks Master.",
            {
                474: "The character does not have this task.",
                475: "Task already completed or too many items submitted.",
                598: "Tasks Master not found on this map.",
            },
            json={
                "code": code,
                "quantity": quantity,
            },
        )

    def task_cancel(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
    ) -> tuple[str, TaskCancelledResponseSchema | None]:
        """Cancel a task for 1 tasks coin."""
        return self._request(
            "POST",
            f"/my/{name}/action/task/cancel",
            TaskCancelledResponseSchema,
            "The task has been successfully cancelled.",
            {
                487: "The character has no task assigned.",
                598: "Tasks Master not found on this map.",
            },
        )

    def give_gold(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        quantity: Annotated[int, Field(description="Gold quantity.", ge=1)],
        character: Annotated[
            str,
            Field(
                description="Character name. The name of the character who will receive the gold.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ],
    ) -> tuple[str, GiveGoldResponseSchema | None]:
        """Give gold to another character in your account on the same map."""
        return self._request(
            "POST",
            f"/my/{name}/action/give/gold",
            GiveGoldResponseSchema,
            "Gold given successfully.",
            {
                492: "The character does not have enough gold.",
            },
            json={
                "quantity": quantity,
                "character": character,
            },
        )

    def give_items(
        self,
        name: Annotated[
            str,
            Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$"),
        ],
        items: Annotated[
            list[SimpleItemSchema], Field(description="List of items to give")
        ],
        character: Annotated[
            str,
            Field(
                description="Character name. The name of the character who will receive the items.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ],
    ) -> tuple[str, GiveItemResponseSchema | None]:
        """Give items to another character in your account on the same map.
        The cooldown will be 3 seconds multiplied by the number of different items given."""
        return self._request(
            "POST",
            f"/my/{name}/action/give/item",
            GiveItemResponseSchema,
            "Items given successfully.",
            {
                404: "Item not found.",
            },
            json={
                "items": items,
                "character": character,
            },
        )
