"""Maps schemas."""

from pydantic import BaseModel

from .common import MapSchema


class StaticDataPage_MapSchema_(BaseModel):
    """StaticDataPage[MapSchema]"""

    data: list[MapSchema]
    total: int
    page: int
    size: int
    pages: int
