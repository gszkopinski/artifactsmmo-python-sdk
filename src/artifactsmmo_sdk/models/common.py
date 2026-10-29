"""Common schemas."""

from enum import Enum


class RewardType(str, Enum):
    """RewardType."""

    BADGE = "badge"
    SKIN = "skin"
    GOLD = "gold"
    ITEM = "item"
