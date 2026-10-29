"""GemsShop."""

from ..base import BaseModule
from ..models.gems_shop import (
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
