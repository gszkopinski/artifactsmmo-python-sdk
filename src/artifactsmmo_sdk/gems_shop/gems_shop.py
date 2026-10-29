"""GemsShop."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.gems_shop import (
    BuySkinResponseSchema,
    GemShopCatalogResponseSchema,
)


class GemsShop(BaseModule):
    """GemsShop."""

    def get_catalog(
        self,
    ) -> tuple[str, GemShopCatalogResponseSchema | None]:
        """Return the gems shop catalog."""
        return self._request(
            "GET",
            "/gems_shop/",
            GemShopCatalogResponseSchema,
            "Successfully fetched gems shop catalog.",
        )

    def buy_skin(
        self,
        code: Annotated[str, Field(description="Code of the skin to purchase.")],
    ) -> tuple[str, BuySkinResponseSchema | None]:
        """Buy a skin from the gems shop using gems."""
        return self._request(
            "POST",
            "/gems_shop/skin",
            BuySkinResponseSchema,
            "Successfully fetched data.",
            {
                404: "Skin not found.",
                551: "You already own this skin.",
                552: "This skin is not available for purchase.",
                563: "Insufficient gems.",
            },
            json={
                "code": code,
            },
        )
