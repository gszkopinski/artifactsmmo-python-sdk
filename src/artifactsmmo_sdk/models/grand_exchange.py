"""GrandExchange schemas."""

from pydantic import BaseModel

from .common import GEOrderSchema


class GEOrderResponseSchema(BaseModel):
    """GEOrderResponseSchema"""

    data: GEOrderSchema
