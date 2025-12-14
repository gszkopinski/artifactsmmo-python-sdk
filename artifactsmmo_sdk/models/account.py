"""Account Schemas."""

from typing import List

from pydantic import BaseModel

from .common import SimpleItemSchema


# ---------------------------------------------------------
# BANK DETAILS
# ---------------------------------------------------------
class BankSchema(BaseModel):
    """Bank Schema."""

    slots: int
    expansions: int
    next_expansion_cost: int
    gold: int


class ListBankDetailsResponseSchema(BaseModel):
    """List Bank Details Response Schema."""

    data: BankSchema


# ---------------------------------------------------------
# BANK ITEM
# ---------------------------------------------------------
class ListBankItemsResponseSchema(BaseModel):
    """List Bank Items Response Schema."""

    data: List[SimpleItemSchema]
    total: int
    page: int
    size: int
    pages: int


# ---------------------------------------------------------
# GRAND EXCHANGE - ORDER
# ---------------------------------------------------------
class GEOrderSchema(BaseModel):
    """Grand Exchange Order Schema."""

    id: str
    seller: str
    code: str
    quantity: int
    price: int
    created_at: str


class GEOrderResponseSchema(BaseModel):
    """Grand Exchange Order Response Schema."""

    data: List[GEOrderSchema]
    total: int
    page: int
    size: int
    pages: int


# ---------------------------------------------------------
# GRAND EXCHANGE - ORDER HISTORY
# ---------------------------------------------------------
class GEOrderHistorySchema(BaseModel):
    """Grand Exchange Order History Schema."""

    order_id: str
    seller: str
    buyer: str
    code: str
    quantity: int
    price: int
    sold_at: str


class GEOrderHistoryResponseSchema(BaseModel):
    """Grand Exchange Order Response Schema."""

    data: List[GEOrderHistorySchema]
    total: int
    page: int
    size: int
    pages: int


# ---------------------------------------------------------
# ACCOUNT - DETAILS
# ---------------------------------------------------------
class AccountDetailsSchema(BaseModel):
    """Account Details Schema."""

    username: str
    email: str
    member: bool
    member_expiration: str | None
    status: str
    badges: List[str]
    skins: List[str]
    gems: int
    event_token: int
    achievements_points: int
    banned: bool
    ban_reason: str


class AccountDetailsResponseSchema(BaseModel):
    """Account Details Response Schema."""

    data: AccountDetailsSchema


# ---------------------------------------------------------
# PASSWORD
# ---------------------------------------------------------
class ChangePasswordResponseSchema(BaseModel):
    """ChangePasswordResponseSchema."""

    message: str
