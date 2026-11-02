"""Seasonal offerings schemas."""

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel

from .actions import CooldownSchema
from .common import CharacterSchema


class OfferingCategory(str, Enum):
    """OfferingCategory."""

    COMBAT = "combat"
    MINING = "mining"
    WOODCUTTING = "woodcutting"
    FISHING = "fishing"
    ALCHEMY = "alchemy"
    WEAPONCRAFTING = "weaponcrafting"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    COOKING = "cooking"


class OfferingTargetType(str, Enum):
    """OfferingTargetType."""

    MONSTER = "monster"
    RESOURCE = "resource"
    CRAFT = "craft"


class SelectedOfferingStatus(str, Enum):
    """SelectedOfferingStatus."""

    ACCEPTED = "accepted"
    COMPLETED = "completed"


class OfferingRequirementSchema(BaseModel):
    """OfferingRequirementSchema"""

    code: str
    quantity: int


class OfferingFavorSchema(BaseModel):
    """OfferingFavorSchema"""

    target_type: OfferingTargetType
    target_code: str
    xp_multiplier: float = 1.5
    drop_multiplier: float = 1.0


class SeasonalOfferingSchema(BaseModel):
    """SeasonalOfferingSchema"""

    id: str
    category: OfferingCategory
    type: OfferingTargetType
    level_min: int
    level_max: int
    requirement: OfferingRequirementSchema
    favor: OfferingFavorSchema


class SelectedOfferingSchema(BaseModel):
    """SelectedOfferingSchema"""

    offering_id: str
    category: OfferingCategory
    status: SelectedOfferingStatus
    accepted_at: datetime
    completed_at: datetime | None = None
    reward_xp: int = 0
    requirement: OfferingRequirementSchema
    favor: OfferingFavorSchema
    expires_at: datetime


class DailySeasonalOfferingsSchema(BaseModel):
    """DailySeasonalOfferingsSchema"""

    date: date
    expires_at: datetime
    skills: list[str]
    xp_reward_percent: int = 25
    offerings: list[SeasonalOfferingSchema]


class DailySeasonalOfferingsResponseSchema(BaseModel):
    """DailySeasonalOfferingsResponseSchema"""

    data: DailySeasonalOfferingsSchema


class CharacterSeasonalOfferingsSchema(DailySeasonalOfferingsSchema):
    """CharacterSeasonalOfferingsSchema"""

    selected_offerings: list[SelectedOfferingSchema]
    completed_categories: list[OfferingCategory]
    active_favors: list[OfferingFavorSchema]


class CharacterSeasonalOfferingsResponseSchema(BaseModel):
    """CharacterSeasonalOfferingsResponseSchema"""

    data: CharacterSeasonalOfferingsSchema


class OfferingRewardSchema(BaseModel):
    """OfferingRewardSchema"""

    category: OfferingCategory
    xp: int


class AcceptOfferingDataSchema(BaseModel):
    """AcceptOfferingDataSchema"""

    cooldown: CooldownSchema
    offering: SeasonalOfferingSchema
    favor_expires_at: datetime
    character: CharacterSchema


class AcceptOfferingResponseSchema(BaseModel):
    """AcceptOfferingResponseSchema"""

    data: AcceptOfferingDataSchema


class CompleteOfferingDataSchema(AcceptOfferingDataSchema):
    """CompleteOfferingDataSchema"""

    reward: OfferingRewardSchema


class CompleteOfferingResponseSchema(BaseModel):
    """CompleteOfferingResponseSchema"""

    data: CompleteOfferingDataSchema
