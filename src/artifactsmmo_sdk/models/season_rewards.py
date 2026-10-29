"""SeasonRewards schemas."""

from pydantic import BaseModel

from .common import RewardType


class SeasonRewardSchema(BaseModel):
    """SeasonRewardSchema"""

    code: str
    type: RewardType
    description: str
    required_points: int
    quantity: int | None = None
    member_required: bool | None = None
    first_only: bool | None = None


class StaticDataPage_SeasonRewardSchema_(BaseModel):
    """StaticDataPage[SeasonRewardSchema]"""

    data: list[SeasonRewardSchema]
    total: int
    page: int
    size: int
    pages: int
