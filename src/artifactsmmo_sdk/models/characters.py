"""Characters schemas."""

from pydantic import BaseModel

from .common import CharacterSchema


class CharacterResponseSchema(BaseModel):
    """CharacterResponseSchema"""

    data: CharacterSchema
