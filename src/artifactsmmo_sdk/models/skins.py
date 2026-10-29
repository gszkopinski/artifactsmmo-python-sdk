"""Skins schemas."""

from pydantic import BaseModel


class SkinSchema(BaseModel):
    """SkinSchema"""

    code: str
    name: str
    description: str
    default: bool
    price: int | None = None


class SkinResponseSchema(BaseModel):
    """SkinResponseSchema"""

    data: SkinSchema


class StaticDataPage_SkinSchema_(BaseModel):
    """StaticDataPage[SkinSchema]"""

    data: list[SkinSchema]
    total: int
    page: int
    size: int
    pages: int
