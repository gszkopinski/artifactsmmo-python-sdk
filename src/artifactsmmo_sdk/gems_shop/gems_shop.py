"""GemsShop."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.gems_shop import (
    ActiveEventResponseSchema,
    BuySkinResponseSchema,
    GemShopCatalogResponseSchema,
    GemShopCustomDesignPurchaseResponseSchema,
    GemShopSubscriptionResponseSchema,
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

    def buy_spawn_event(
        self,
        code: Annotated[str, Field(description="Code of the event to spawn")],
    ) -> tuple[str, ActiveEventResponseSchema | None]:
        """Spawn an event from the gems shop using gems."""
        return self._request(
            "POST",
            "/gems_shop/spawn_event",
            ActiveEventResponseSchema,
            "Successfully fetched data.",
            {
                404: "Event not found.",
                563: "Insufficient gems.",
                564: "Event already active or maximum active events reached.",
                566: "This event is on cooldown and cannot be spawned yet.",
                571: "This event is not available for purchase.",
            },
            json={
                "code": code,
            },
        )

    def buy_subscription(
        self,
    ) -> tuple[str, GemShopSubscriptionResponseSchema | None]:
        """Buy or extend membership by 30 days using gems. Unavailable while a Stripe subscription is active."""
        return self._request(
            "POST",
            "/gems_shop/subscription",
            GemShopSubscriptionResponseSchema,
            "Successfully fetched data.",
            {
                563: "Insufficient gems.",
                573: "An active Stripe subscription cannot be extended with gems or member tokens.",
            },
        )

    def buy_custom_design(
        self,
        code: Annotated[
            str, Field(description="Code of the custom design to purchase.")
        ],
    ) -> tuple[str, GemShopCustomDesignPurchaseResponseSchema | None]:
        """Buy a custom design using gems."""
        return self._request(
            "POST",
            "/gems_shop/buy_custom_design",
            GemShopCustomDesignPurchaseResponseSchema,
            "Successfully fetched data.",
            {
                404: "Custom design not found.",
                563: "Insufficient gems.",
            },
            json={
                "code": code,
            },
        )
