"""Leaderboard schemas."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class AccountLeaderboardSchema(BaseModel):
    """AccountLeaderboardSchema"""

    position: int
    account: str
    member: bool
    achievements_points: int
    completed_at: datetime | None = None
    gold: int


class AccountLeaderboardType(str, Enum):
    """AccountLeaderboardType."""

    ACHIEVEMENTS_POINTS = "achievements_points"
    GOLD = "gold"


class CharacterLeaderboardSchema(BaseModel):
    """CharacterLeaderboardSchema"""

    position: int
    name: str
    account: str
    member: bool
    skin: str
    level: int
    total_xp: int
    mining_level: int
    mining_total_xp: int
    woodcutting_level: int
    woodcutting_total_xp: int
    fishing_level: int
    fishing_total_xp: int
    weaponcrafting_level: int
    weaponcrafting_total_xp: int
    gearcrafting_level: int
    gearcrafting_total_xp: int
    jewelrycrafting_level: int
    jewelrycrafting_total_xp: int
    cooking_level: int
    cooking_total_xp: int
    alchemy_level: int
    alchemy_total_xp: int
    gold: int


class CharacterLeaderboardType(str, Enum):
    """CharacterLeaderboardType."""

    COMBAT = "combat"
    WOODCUTTING = "woodcutting"
    MINING = "mining"
    FISHING = "fishing"
    WEAPONCRAFTING = "weaponcrafting"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    COOKING = "cooking"
    ALCHEMY = "alchemy"


class AccountLeaderboardSchemaPage(BaseModel):
    """DataPage[AccountLeaderboardSchema]"""

    data: list[AccountLeaderboardSchema]
    total: int
    page: int
    size: int
    pages: int


class CharacterLeaderboardSchemaPage(BaseModel):
    """DataPage[CharacterLeaderboardSchema]"""

    data: list[CharacterLeaderboardSchema]
    total: int
    page: int
    size: int
    pages: int
