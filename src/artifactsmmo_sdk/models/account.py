"""Account schemas."""

from pydantic import BaseModel


class BankSchema(BaseModel):
    """BankSchema"""

    slots: int
    expansions: int
    next_expansion_cost: int
    gold: int


class BankResponseSchema(BaseModel):
    """BankResponseSchema"""

    data: BankSchema
