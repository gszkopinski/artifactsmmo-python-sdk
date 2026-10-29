"""Account schemas."""

from pydantic import BaseModel

from .common import SimpleItemSchema


class BankSchema(BaseModel):
    """BankSchema"""

    slots: int
    expansions: int
    next_expansion_cost: int
    gold: int


class BankResponseSchema(BaseModel):
    """BankResponseSchema"""

    data: BankSchema


class SimpleItemSchemaPage(BaseModel):
    """DataPage[SimpleItemSchema]"""

    data: list[SimpleItemSchema]
    total: int
    page: int
    size: int
    pages: int
