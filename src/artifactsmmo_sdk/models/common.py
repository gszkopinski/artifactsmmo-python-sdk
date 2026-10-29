"""Common schemas."""

from enum import Enum

from pydantic import BaseModel


class RewardType(str, Enum):
    """RewardType."""

    BADGE = "badge"
    SKIN = "skin"
    GOLD = "gold"
    ITEM = "item"


class SimpleItemSchema(BaseModel):
    """SimpleItemSchema"""

    code: str
    quantity: int
