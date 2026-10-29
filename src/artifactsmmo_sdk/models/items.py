"""Items schemas."""

from pydantic import BaseModel

from .common import ItemSchema


class ItemResponseSchema(BaseModel):
    """ItemResponseSchema"""

    data: ItemSchema


class StaticDataPage_ItemSchema_(BaseModel):
    """StaticDataPage[ItemSchema]"""

    data: list[ItemSchema]
    total: int
    page: int
    size: int
    pages: int
