"""Token Schemas."""

from pydantic import BaseModel


class TokenResponseSchema(BaseModel):
    """Token Response Schema."""

    token: str
