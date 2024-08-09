"""Actions."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.actions import (
    BankItemResponseSchema,
    CharacterFightDataResponseSchema,
    CharacterMovementDataResponseSchema,
    CharactersResponseSchema,
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
)


class Actions:
    """Characters."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def move(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        x: Annotated[int, Field(description="The x coordinate of the destination.")],
        y: Annotated[int, Field(description="The y coordinate of the destination.")],
    ) -> Tuple[str, CharacterMovementDataResponseSchema | None]:
        """Move a character on the map using the map's X and Y position."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/move",
                json={
                    "x": x,
                    "y": y,
                },
            )

            response.raise_for_status()

            return (
                "The character has moved successfully.",
                CharacterMovementDataResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Map not found.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 490:
                    return "Character already at destination.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case _:
                    return f"Unknown error: {error}", None

    def equip_item(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        code: Annotated[str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")],
        slot: Annotated[SlotEnum, Field(description="Item slot.")],
    ) -> Tuple[str, EquipRequestResponseSchema | None]:
        """Equip an item on your character."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/equip",
                json={
                    "code": code,
                    "slot": slot,
                },
            )

            response.raise_for_status()

            return (
                "The item has been successfully equipped on your character.",
                EquipRequestResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 485:
                    return "This item is already equipped.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 491:
                    return "Slot is not empty.", None
                case 496:
                    return "Character level is insufficient.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case _:
                    return f"Unknown error: {error}", None

    def unequip_item(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        slot: Annotated[SlotEnum, Field(description="Item slot.")],
    ) -> Tuple[str, EquipRequestResponseSchema | None]:
        """Unequip an item on your character."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/unequip",
                json={
                    "slot": slot,
                },
            )

            response.raise_for_status()

            return (
                "The item has been successfully unequipped and added in his inventory.",
                EquipRequestResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 491:
                    return "Slot is not empty.", None
                case 497:
                    return "Character inventory is full.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case _:
                    return f"Unknown error: {error}", None

    def fight(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, CharacterFightDataResponseSchema | None]:
        """Start a fight against a monster on the character's map."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/fight",
            )

            response.raise_for_status()

            return (
                "The fight ended successfully.",
                CharacterFightDataResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 497:
                    return "Character inventory is full.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Monster not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def gathering(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, SkillDataResponseSchema | None]:
        """Harvest a resource on the character's map."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/gathering",
            )

            response.raise_for_status()

            return (
                "The resource has been successfully gathered.",
                SkillDataResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 493:
                    return "Not skill level required.", None
                case 497:
                    return "Character inventory is full.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Resource not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def crafting(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        code: Annotated[str, Field(description="Craft code.", pattern="^[a-zA-Z0-9_-]+$")],
        quantity: Annotated[int, Field(description="Quantity of items to craft.", ge=1, default=1)] = 1,
    ) -> Tuple[str, SkillDataResponseSchema | None]:
        """Crafting an item. The character must be on a map with a workshop."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/crafting",
                json={
                    "code": code,
                    "quantity": quantity,
                },
            )

            response.raise_for_status()

            return (
                "The item was successfully crafted.",
                SkillDataResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Craft not found.", None
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 493:
                    return "Not skill level required.", None
                case 497:
                    return "Character inventory is full.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Workshop not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def deposit_bank(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        code: Annotated[str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, default=1)] = 1,
    ) -> Tuple[str, BankItemResponseSchema | None]:
        """Deposit an item in a bank on the character's map."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/bank/deposit",
                json={
                    "code": code,
                    "quantity": quantity,
                },
            )

            response.raise_for_status()

            return (
                "Item successfully deposited in your bank.",
                BankItemResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Bank not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def deposit_bank_gold(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, default=1)] = 1,
    ) -> Tuple[str, GoldTransactionResponseSchema | None]:
        """Deposit golds in a bank on the character's map."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/bank/deposit/gold",
                json={
                    "quantity": quantity,
                },
            )

            response.raise_for_status()

            return (
                "Golds successfully deposited in your bank.",
                GoldTransactionResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 492:
                    return "Insufficient golds on your character.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Bank not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def recycling(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        code: Annotated[str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")],
        quantity: Annotated[int, Field(description="Quantity of items to recycle.", ge=1, default=1)] = 1,
    ) -> Tuple[str, RecyclingDataResponseSchema | None]:
        """Recyling an item. The character must be on a map with a workshop (only for equipments and weapons)."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/recycling",
                json={
                    "code": code,
                    "quantity": quantity,
                },
            )

            response.raise_for_status()

            return (
                "The items were successfully recycled.",
                RecyclingDataResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case 473:
                    return "Quantity of items to recycle.", None
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 493:
                    return "Not skill level required.", None
                case 497:
                    return "Character inventory is full.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Workshop not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def withdraw_bank(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        code: Annotated[str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, default=1)] = 1,
    ) -> Tuple[str, BankItemResponseSchema | None]:
        """Take an item from your bank and put it in the character's inventory."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/bank/withdraw",
                json={
                    "code": code,
                    "quantity": quantity,
                },
            )

            response.raise_for_status()

            return (
                "Item successfully withdraw from your bank.",
                BankItemResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 497:
                    return "Character inventory is full.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Bank not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def withdraw_bank_gold(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, default=1)] = 1,
    ) -> Tuple[str, GoldTransactionResponseSchema | None]:
        """Withdraw gold from your bank."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/bank/withdraw/gold",
                json={
                    "quantity": quantity,
                },
            )

            response.raise_for_status()

            return (
                "Golds successfully withdraw from your bank.",
                GoldTransactionResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 460:
                    return "Insufficient golds in your bank.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Bank not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def ge_buy_item(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        code: Annotated[str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")],
        price: Annotated[int, Field(description="Item quantity.", ge=1)],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, le=50, default=1)] = 1,
    ) -> Tuple[str, GETransactionResponseSchema | None]:
        """Buy an item at the Grand Exchange on the character's map."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/ge/buy",
                json={
                    "code": code,
                    "quantity": quantity,
                    "price": price,
                },
            )

            response.raise_for_status()

            return (
                "Item successfully buy from the Grand Exchange.",
                GETransactionResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 480:
                    return "No stock for this item.", None
                case 482:
                    return "No item at this price.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 492:
                    return "Insufficient golds on your character.", None
                case 497:
                    return "Character inventory is full.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Grand Exchange not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def ge_sell_item(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        code: Annotated[str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")],
        price: Annotated[int, Field(description="Item quantity.", ge=1)],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, le=50, default=1)] = 1,
    ) -> Tuple[str, GETransactionResponseSchema | None]:
        """Sell an item at the Grand Exchange on the character's map."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/ge/sell",
                json={
                    "code": code,
                    "quantity": quantity,
                    "price": price,
                },
            )

            response.raise_for_status()

            return (
                "Item successfully sell at the Grand Exchange.",
                GETransactionResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 482:
                    return "No item at this price.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Grand Exchange not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def accept_new_task(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, TaskDataResponseSchema | None]:
        """Accept a new task."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/task/new",
            )

            response.raise_for_status()

            return (
                "New task successfully accepted.",
                TaskDataResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 489:
                    return "Character already has a task.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Tasks Master not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def complete_task(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, TaskRewardDataResponseSchema | None]:
        """Complete a task."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/task/complete",
            )

            response.raise_for_status()

            return (
                "The task has been successfully completed.",
                TaskRewardDataResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 487:
                    return "Character has no task.", None
                case 488:
                    return "Character has not completed the task.", None
                case 497:
                    return "Character inventory is full.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Tasks Master not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def task_exchange(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, TaskRewardDataResponseSchema | None]:
        """Exchange 3 tasks coins for a random reward. Rewards are exclusive resources for crafting items."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/task/exchange",
            )

            response.raise_for_status()

            return (
                "The tasks coins have been successfully exchanged.",
                TaskRewardDataResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 497:
                    return "Character inventory is full..", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case 598:
                    return "Tasks Master not found on this map.", None
                case _:
                    return f"Unknown error: {error}", None

    def delete_item(
        self,
        name: Annotated[str, Field(description="Name of your character.", pattern="^[a-zA-Z0-9_-]+$")],
        code: Annotated[str, Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$")],
        quantity: Annotated[int, Field(description="Item quantity.", ge=1, default=1)] = 1,
    ) -> Tuple[str, DeleteItemResponseSchema | None]:
        """Delete an item from your character's inventory.."""
        try:
            response = self.session.post(
                url=f"{self.api_url}/my/{name}/action/recycling",
                json={
                    "code": code,
                    "quantity": quantity,
                },
            )

            response.raise_for_status()

            return (
                "Item successfully deleted from your character.",
                DeleteItemResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 478:
                    return "Missing item or insufficient quantity in your inventory.", None
                case 486:
                    return "Character is locked. Action is already in progress.", None
                case 498:
                    return "Character not found.", None
                case 499:
                    return "Character in cooldown.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_all_character_logs(
        self,
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[int, Field(description="Page size.", ge=1, le=100, default=50)] = 50,
    ) -> Tuple[str, LogsResponseSchema | None]:
        """Get all character logs."""
        try:
            parameters = f"page={page}"
            parameters += f"&size={size}"

            response = response = self.session.get(
                url=f"{self.api_url}/my/logs?{parameters}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched logs.",
                LogsResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Logs not found.", None
                case 498:
                    return "Character not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_my_characters(
        self,
    ) -> Tuple[str, CharactersResponseSchema | None]:
        """List of your characters."""
        try:
            response = response = self.session.get(
                url=f"{self.api_url}/my/characters",
            )

            response.raise_for_status()

            return (
                "Successfully fetched characters.",
                CharactersResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Character not found.", None
                case _:
                    return f"Unknown error: {error}", None
