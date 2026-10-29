"""Badges schemas."""

from pydantic import BaseModel


class BadgeSchema(BaseModel):
    """BadgeSchema"""

    code: str
    season: int | None = None
    description: str


class StaticDataPage_BadgeSchema_(BaseModel):
    """StaticDataPage[BadgeSchema]"""

    data: list[BadgeSchema]
    total: int
    page: int
    size: int
    pages: int
