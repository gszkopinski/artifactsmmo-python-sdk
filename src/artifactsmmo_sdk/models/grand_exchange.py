"""Grand Exchange Models."""

from pydantic import BaseModel


class GEItemSchema(BaseModel):
    """GE Item Schema."""

    code: str
    stock: int
    sell_price: int
    buy_price: int


class GEItemResponseSchema(BaseModel):
    """GE Item Repose Schema."""

    data: GEItemSchema


class ListActiveEventResponseSchema(BaseModel):
    """List Active Event Response Schema."""

    data: list[GEItemSchema]
    total: int
    page: int
    size: int
    pages: int
