"""Npcs schemas."""

from enum import Enum

from pydantic import BaseModel


class NPCType(str, Enum):
    """NPCType."""

    MERCHANT = "merchant"
    TRADER = "trader"


class SimpleNPCItemSchema(BaseModel):
    """SimpleNPCItemSchema"""

    code: str
    currency: str
    buy_price: int | None = None
    sell_price: int | None = None


class NPCSchema(BaseModel):
    """NPCSchema"""

    name: str
    code: str
    description: str
    type: NPCType
    items: list[SimpleNPCItemSchema] | None = None


class StaticDataPage_NPCSchema_(BaseModel):
    """StaticDataPage[NPCSchema]"""

    data: list[NPCSchema]
    total: int
    page: int
    size: int
    pages: int
