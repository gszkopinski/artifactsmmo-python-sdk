"""Achievements."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.achievements import (
    AchievementResponseSchema,
    StaticDataPage_AchievementSchema_,
)
from ..models.common import (
    AchievementType,
)


class Achievements(BaseModule):
    """Achievements."""

    def get_all_achievements(
        self,
        type: Annotated[
            AchievementType | None, Field(description="Type of achievements.")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_AchievementSchema_ | None]:
        """List of all achievements."""
        return self._request(
            "GET",
            "/achievements",
            StaticDataPage_AchievementSchema_,
            "Successfully fetched achievements.",
            params={
                "type": type,
                "page": page,
                "size": size,
            },
        )

    def get_achievement(
        self,
        code: Annotated[
            str,
            Field(
                description="The code of the achievement.", pattern="^[a-zA-Z0-9_-]+$"
            ),
        ],
    ) -> tuple[str, AchievementResponseSchema | None]:
        """Retrieve the details of an achievement."""
        return self._request(
            "GET",
            f"/achievements/{code}",
            AchievementResponseSchema,
            "Successfully fetched achievement.",
            {
                404: "achievement not found.",
            },
        )
