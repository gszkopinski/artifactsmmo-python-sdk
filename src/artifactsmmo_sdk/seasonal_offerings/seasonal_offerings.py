"""SeasonalOfferings."""

from ..base import BaseModule
from ..models.seasonal_offerings import DailySeasonalOfferingsResponseSchema


class SeasonalOfferings(BaseModule):
    """SeasonalOfferings."""

    def get_daily_seasonal_offerings(
        self,
    ) -> tuple[str, DailySeasonalOfferingsResponseSchema | None]:
        """Return the worldwide seasonal offerings available for the current UTC day."""
        return self._request(
            "GET",
            "/seasonal_offerings",
            DailySeasonalOfferingsResponseSchema,
            "Successfully fetched seasonal offerings.",
            {
                575: "This seasonal offering is not available.",
            },
        )
