"""Actions."""

import requests

from pydantic import Field

from ..models.actions import (
    ActionEquipItemResponseSchema,
    ActionFightResponseSchema,
    ActionMoveResponseSchema,
    BankItemResponseSchema,
    DeleteItemResponseSchema,
    GETransactionResponseSchema,
    LogsResponseSchema,
    SkillDataSchema,
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

    def move(self, name: str, x: int, y: int) -> ActionMoveResponseSchema:
        """Move."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/move",
            json={
                "x": x,
                "y": y,
            },
        )

        response.raise_for_status()

        return ActionMoveResponseSchema.model_validate(response.json())

    def equip_item(
        self,
        name: str,
        code: str,
        slot: str,
    ) -> ActionEquipItemResponseSchema:
        """Equip Item."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/equip",
            json={
                "code": code,
                "slot": slot,
            },
        )

        response.raise_for_status()

        return ActionEquipItemResponseSchema.model_validate(response.json())

    def unequip_item(
        self,
        name: str,
        slot: str,
    ) -> ActionEquipItemResponseSchema:
        """Equip Item."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/unequip",
            json={
                "slot": slot,
            },
        )

        response.raise_for_status()

        return ActionEquipItemResponseSchema.model_validate(response.json())

    def fight(
        self,
        name: str,
    ) -> ActionFightResponseSchema:
        """Fight."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/fight",
        )

        response.raise_for_status()

        return ActionFightResponseSchema.model_validate(response.json())

    def gathering(
        self,
        name: str,
    ) -> SkillDataSchema:
        """Gathering."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/gathering",
        )

        response.raise_for_status()

        return SkillDataSchema.model_validate(response.json())

    def crafting(
        self,
        name: str,
        code: str,
        quantity: int,
    ) -> SkillDataSchema:
        """Crafting."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/crafting",
            json={
                "code": code,
                "quantity": quantity,
            },
        )

        response.raise_for_status()

        return SkillDataSchema.model_validate(response.json())

    def deposit_bank(
        self,
        name: str,
        code: str,
        quantity: int,
    ) -> BankItemResponseSchema:
        """Deposit bank."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/bank/deposit",
            json={
                "code": code,
                "quantity": quantity,
            },
        )

        response.raise_for_status()

        return BankItemResponseSchema.model_validate(response.json())

    def deposit_bank_gold(
        self,
        name: str,
        quantity: int,
    ) -> BankItemResponseSchema:
        """Deposit golds in a bank on the character's map."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/bank/deposit/gold",
            json={
                "quantity": quantity,
            },
        )

        response.raise_for_status()

        return BankItemResponseSchema.model_validate(response.json())

    def recycling(
        self,
        name: str,
        code: str,
        quantity: int,
    ) -> SkillDataSchema:
        """Crafting."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/recycling",
            json={
                "code": code,
                "quantity": quantity,
            },
        )

        response.raise_for_status()

        return SkillDataSchema.model_validate(response.json())

    def withdraw_bank(
        self,
        name: str,
        code: str,
        quantity: int,
    ) -> BankItemResponseSchema:
        """Take an item from your bank and put it in the character's inventory."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/bank/deposit",
            json={
                "code": code,
                "quantity": quantity,
            },
        )

        response.raise_for_status()

        return BankItemResponseSchema.model_validate(response.json())

    def withdraw_bank_gold(
        self,
        name: str,
        quantity: int,
    ) -> BankItemResponseSchema:
        """Withdraw gold from your bank."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/bank/deposit/gold",
            json={
                "quantity": quantity,
            },
        )

        response.raise_for_status()

        return BankItemResponseSchema.model_validate(response.json())

    def ge_buy_item(
        self,
        name: str,
        code: str,
        quantity: int,
        price: int,
    ) -> GETransactionResponseSchema:
        """Buy an item at the Grand Exchange on the character's map."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/ge/buy",
            json={
                "code": code,
                "quantity": quantity,
                "price": price,
            },
        )

        response.raise_for_status()

        return GETransactionResponseSchema.model_validate(response.json())

    def ge_sell_item(
        self,
        name: str,
        code: str,
        quantity: int,
        price: int,
    ) -> GETransactionResponseSchema:
        """Sell an item at the Grand Exchange on the character's map."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/ge/sell",
            json={
                "code": code,
                "quantity": quantity,
                "price": price,
            },
        )

        response.raise_for_status()

        return GETransactionResponseSchema.model_validate(response.json())

    def accept_new_task(
        self,
        name: str = Field(description="Name of your character", pattern="^[a-zA-Z0-9_-]+$"),
    ) -> TaskDataResponseSchema:
        """Accept a new task."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/task/new",
        )

        response.raise_for_status()

        return TaskDataResponseSchema.model_validate(response.json())

    def complete_task(
        self,
        name: str = Field(description="Name of your character", pattern="^[a-zA-Z0-9_-]+$"),
    ) -> TaskRewardDataResponseSchema:
        """Complete a task."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/task/complete",
        )

        response.raise_for_status()

        return TaskRewardDataResponseSchema.model_validate(response.json())

    def task_exchange(
        self,
        name: str = Field(description="Name of your character", pattern="^[a-zA-Z0-9_-]+$"),
    ) -> TaskRewardDataResponseSchema:
        """Exchange 3 tasks coins for a random reward. Rewards are exclusive resources for crafting items."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/task/exchange",
        )

        response.raise_for_status()

        return TaskRewardDataResponseSchema.model_validate(response.json())

    def delete_item(
        self,
        name: str = Field(description="Name of your character", pattern="^[a-zA-Z0-9_-]+$"),
        code: str = Field(description="Item code.", pattern="^[a-zA-Z0-9_-]+$"),
        quantity: int = Field(description="Item quantity.", ge=1),
    ) -> DeleteItemResponseSchema:
        """Crafting."""
        response = self.session.post(
            url=f"{self.api_url}/my/{name}/action/recycling",
            json={
                "code": code,
                "quantity": quantity,
            },
        )

        response.raise_for_status()

        return DeleteItemResponseSchema.model_validate(response.json())

    def get_character_logs(
        self,
        name: str,
        page: int = 1,
        size: int = 50,
    ) -> LogsResponseSchema:
        """Get character logs."""
        response = response = self.session.get(
            url=f"{self.api_url}/my/{name}/logs?page={page},size={size}",
        )

        response.raise_for_status()

        return LogsResponseSchema.model_validate(response.json())
