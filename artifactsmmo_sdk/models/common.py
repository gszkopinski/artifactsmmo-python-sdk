"""Common Models."""

from pydantic import BaseModel


class DropRateSchema(BaseModel):
    """Drop Rate Schema."""

    code: str
    rate: int
    min_quantity: int
    max_quantity: int


# Map Content Schema
class MapContentSchema(BaseModel):
    """Map Content Schema."""

    type: str
    code: str


class PointOfInterest(BaseModel):
    """Point of Interest."""

    x: int
    y: int
    description: str
