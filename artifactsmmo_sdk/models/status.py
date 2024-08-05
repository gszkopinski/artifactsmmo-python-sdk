"""Status Models."""

from typing import List

from pydantic import BaseModel


class AnnouncementSchema(BaseModel):
    """Announcement Schema."""

    message: str
    created_at: str


class StatusSchema(BaseModel):
    """Status Schema."""

    status: str
    version: str
    characters_online: int
    announcements: List[AnnouncementSchema]
    last_wipe: str
    next_wipe: str


class StatusReponseSchema(BaseModel):
    """Status Response Schema."""

    data: StatusSchema
