"""Accounts Schemas."""

from pydantic import BaseModel


class AccountsResponseSchema(BaseModel):
    """Accounts Response Schema."""

    message: str
