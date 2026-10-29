"""Common schemas."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class GEOrderType(str, Enum):
    """GEOrderType."""

    SELL = "sell"
    BUY = "buy"


class GEOrderSchema(BaseModel):
    """GEOrderSchema"""

    id: str
    type: GEOrderType
    account: str | None = None
    code: str
    quantity: int
    price: int
    created_at: datetime


class GEOrderSchemaPage(BaseModel):
    """DataPage[GEOrderSchema]"""

    data: list[GEOrderSchema]
    total: int
    page: int
    size: int
    pages: int


class RewardType(str, Enum):
    """RewardType."""

    BADGE = "badge"
    SKIN = "skin"
    GOLD = "gold"
    ITEM = "item"


class SimpleItemSchema(BaseModel):
    """SimpleItemSchema"""

    code: str
    quantity: int
