"""Account."""

from typing import Annotated, Literal

from pydantic import Field

from ..base import BaseModule
from ..models.account import (
    BankResponseSchema,
    CheckoutResponseWrapperSchema,
    GemTransactionListResponseSchema,
    MemberTokenSubscriptionResponseSchema,
    MyAccountDetailsSchema,
    PendingItemSchemaPage,
    PurchaseHistoryListResponseSchema,
    RateLimitsSchema,
    SimpleItemSchemaPage,
    StripeSubscriptionPlan,
    SubscriptionResponseSchema,
)
from ..models.common import (
    GEOrderHistorySchemaPage,
    GEOrderSchemaPage,
    GEOrderType,
    ResponseSchema,
)


class Account(BaseModule):
    """Account."""

    def get_bank_details(
        self,
    ) -> tuple[str, BankResponseSchema | None]:
        """Fetch bank details."""
        return self._request(
            "GET",
            "/my/bank",
            BankResponseSchema,
            "Successfully fetched data.",
        )

    def get_bank_items(
        self,
        item_code: Annotated[
            str | None,
            Field(
                description="Item to search in your bank.", pattern="^[a-zA-Z0-9_-]+$"
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, SimpleItemSchemaPage | None]:
        """Fetch all items in your bank."""
        return self._request(
            "GET",
            "/my/bank/items",
            SimpleItemSchemaPage,
            "Successfully fetched data.",
            params={
                "item_code": item_code,
                "page": page,
                "size": size,
            },
        )

    def get_ge_sell_orders(
        self,
        code: Annotated[
            str | None,
            Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$"),
        ] = None,
        type: Annotated[
            GEOrderType | None, Field(description="Filter by order type (sell or buy).")
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, GEOrderSchemaPage | None]:
        """Fetch your orders details (sell and buy orders)."""
        return self._request(
            "GET",
            "/my/grandexchange/orders",
            GEOrderSchemaPage,
            "Successfully fetched data.",
            params={
                "code": code,
                "type": type,
                "page": page,
                "size": size,
            },
        )

    def get_ge_sell_history(
        self,
        id: Annotated[
            str | None,
            Field(
                description="Order ID to search in your history.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        code: Annotated[
            str | None,
            Field(
                description="Item to search in your history.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, GEOrderHistorySchemaPage | None]:
        """Fetch your transaction history of the last 7 days (buy and sell orders)."""
        return self._request(
            "GET",
            "/my/grandexchange/history",
            GEOrderHistorySchemaPage,
            "Successfully fetched data.",
            params={
                "id": id,
                "code": code,
                "page": page,
                "size": size,
            },
        )

    def get_account_details(
        self,
    ) -> tuple[str, MyAccountDetailsSchema | None]:
        """Fetch account details."""
        return self._request(
            "GET",
            "/my/details",
            MyAccountDetailsSchema,
            "Successfully fetched data.",
        )

    def get_pending_items(
        self,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=100)] = 50,
    ) -> tuple[str, PendingItemSchemaPage | None]:
        """Retrieve all unclaimed pending items for your account.

        These are items from various sources (achievements, grand exchange, events, etc.)
        that can be claimed by any character on your account using /my/{name}/action/claim/{id}."""
        return self._request(
            "GET",
            "/my/pending_items",
            PendingItemSchemaPage,
            "Successfully fetched pending items.",
            params={
                "page": page,
                "size": size,
            },
        )

    def get_rate_limits(
        self,
    ) -> tuple[str, RateLimitsSchema | None]:
        """Get all rate limits."""
        return self._request(
            "GET",
            "/my/rates",
            RateLimitsSchema,
            "Successfully fetched rate limits.",
        )

    def change_password(
        self,
        current_password: Annotated[
            str, Field(description="Your password.", pattern="^[^\\s]+$")
        ],
        new_password: Annotated[
            str, Field(description="New password.", pattern="^[^\\s]+$")
        ],
    ) -> tuple[str, ResponseSchema | None]:
        """Change your account password. Changing the password reset the account token."""
        return self._request(
            "POST",
            "/my/change_password",
            ResponseSchema,
            "Password changed successfully.",
            {
                458: "Please use a different password.",
                459: "The current password you entered is invalid.",
            },
            json={
                "current_password": current_password,
                "new_password": new_password,
            },
        )

    def change_email(
        self,
        current_email: Annotated[str, Field(description="Your current email.")],
        new_email: Annotated[str, Field(description="New email.")],
    ) -> tuple[str, ResponseSchema | None]:
        """Change your account email."""
        return self._request(
            "POST",
            "/my/change_email",
            ResponseSchema,
            "Email changed successfully.",
            {
                457: "This email is already in use.",
                463: "Please use a different email.",
            },
            json={
                "current_email": current_email,
                "new_email": new_email,
            },
        )

    def get_my_subscription(
        self,
    ) -> tuple[str, SubscriptionResponseSchema | None]:
        """Get current subscription details."""
        return self._request(
            "GET",
            "/my/subscription",
            SubscriptionResponseSchema,
            "Successfully fetched data.",
            {
                404: "Subscription not found.",
            },
        )

    def subscribe_with_stripe(
        self,
        plan: Annotated[
            StripeSubscriptionPlan,
            Field(description="Stripe membership plan to purchase."),
        ],
        recurring: Annotated[
            bool | None,
            Field(
                description="Whether to create a recurring Stripe subscription. Set to false to buy membership time once."
            ),
        ] = None,
    ) -> tuple[str, CheckoutResponseWrapperSchema | None]:
        """Subscribe to become a member and unlock the benefits tied to your selected plan.
        You will receive a secure Stripe checkout URL to complete the payment."""
        return self._request(
            "POST",
            "/my/subscribe/stripe",
            CheckoutResponseWrapperSchema,
            "Successfully fetched data.",
            {
                565: "You already have an active subscription.",
                573: "An active Stripe subscription cannot be extended with gems or member tokens.",
            },
            json={
                "plan": plan,
                "recurring": recurring,
            },
        )

    def subscribe_with_member_token(
        self,
    ) -> tuple[str, MemberTokenSubscriptionResponseSchema | None]:
        """Redeem a member token to start or extend membership by 30 days.
        Member tokens are manually granted as rewards for events.
        Member tokens cannot be redeemed while a Stripe subscription is active."""
        return self._request(
            "POST",
            "/my/subscribe/member_token",
            MemberTokenSubscriptionResponseSchema,
            "Successfully fetched data.",
            {
                572: "Insufficient member tokens.",
                573: "An active Stripe subscription cannot be extended with gems or member tokens.",
            },
        )

    def cancel_subscription(
        self,
    ) -> tuple[str, ResponseSchema | None]:
        """Cancel subscription at the end of the current billing period."""
        return self._request(
            "POST",
            "/my/subscribe/cancel",
            ResponseSchema,
            "Successfully fetched data.",
            {
                404: "Subscription not found.",
            },
        )

    def get_my_purchase_history(
        self,
    ) -> tuple[str, PurchaseHistoryListResponseSchema | None]:
        """List all purchases (subscriptions and gem packs)."""
        return self._request(
            "GET",
            "/my/purchase_history",
            PurchaseHistoryListResponseSchema,
            "Successfully fetched data.",
        )

    def get_my_gems_history(
        self,
    ) -> tuple[str, GemTransactionListResponseSchema | None]:
        """List all gem credits and debits."""
        return self._request(
            "GET",
            "/my/gems_history",
            GemTransactionListResponseSchema,
            "Successfully fetched data.",
        )

    def buy_gems(
        self,
        quantity: Annotated[
            Literal[500, 1100, 2400, 6125, 12500],
            Field(description="Number of gems to purchase."),
        ],
    ) -> tuple[str, CheckoutResponseWrapperSchema | None]:
        """Purchase gems. Returns a Stripe checkout URL for payment."""
        return self._request(
            "POST",
            "/my/buy_gems",
            CheckoutResponseWrapperSchema,
            "Successfully fetched data.",
            {
                404: "Gem pack not found.",
            },
            json={
                "quantity": quantity,
            },
        )
