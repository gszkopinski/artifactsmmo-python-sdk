"""SeasonRewards."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.common import (
    RewardType,
)
from ..models.season_rewards import (
    StaticDataPage_SeasonRewardSchema_,
)


class SeasonRewards(BaseModule):
    """SeasonRewards."""

    def get_all_season_rewards(
        self,
        type: Annotated[
            RewardType | None, Field(description="Filter by reward type.")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_SeasonRewardSchema_ | None]:
        """List of all rewards for the current season."""
        return self._request(
            "GET",
            "/season_rewards",
            StaticDataPage_SeasonRewardSchema_,
            "Successfully fetched season rewards.",
            params={
                "type": type,
                "page": page,
                "size": size,
            },
        )

    def get_season_rewards_by_code(
        self,
        code: Annotated[
            str,
            Field(
                description="The code of the season reward.", pattern="^[a-zA-Z0-9_-]+$"
            ),
        ],
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_SeasonRewardSchema_ | None]:
        """List all season rewards matching a specific code."""
        return self._request(
            "GET",
            f"/season_rewards/{code}",
            StaticDataPage_SeasonRewardSchema_,
            "Successfully fetched season rewards.",
            params={
                "page": page,
                "size": size,
            },
        )
