"""Items Schemas."""

from typing import Optional

from pydantic import BaseModel

from .actions import ItemSchema


# Item Content Schema
class GEItemSchema(BaseModel):
    """Item Content Schema."""

    code: str
    stock: int
    sell_price: int
    buy_price: int


# Single Item Schema
class SingleItemSchema(BaseModel):
    """Single Item Schema."""

    item: ItemSchema
    ge: Optional[GEItemSchema] = None


# Single Item Response Schema
class SingleItemResponseSchema(BaseModel):
    """Single Item Response Schema."""

    data: SingleItemSchema
