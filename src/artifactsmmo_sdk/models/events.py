"""Events schemas."""

from pydantic import BaseModel

from .common import ActiveEventSchema


class StaticDataPage_ActiveEventSchema_(BaseModel):
    """StaticDataPage[ActiveEventSchema]"""

    data: list[ActiveEventSchema]
    total: int
    page: int
    size: int
    pages: int
