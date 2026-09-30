"""Status Models."""

from pydantic import BaseModel


class SeasonBadgeSchema(BaseModel):
    """Season Badge Schema."""

    code: str
    description: str
    required_points: int


class SeasonSkinSchema(BaseModel):
    """Season Skin Schema."""

    code: str
    description: str
    required_points: int


class SeasonSchema(BaseModel):
    """Season Schema."""

    name: str
    number: int
    start_date: str
    badges: list[SeasonBadgeSchema]
    skins: list[SeasonSkinSchema]


class RateLimitSchema(BaseModel):
    """Rate Limit Schema."""

    type: str
    value: str


class StatusSchema(BaseModel):
    """Status Schema."""

    version: str
    server_time: str
    max_level: int
    max_skill_level: int
    characters_online: int
    season: SeasonSchema
    rate_limits: list[RateLimitSchema]


class StatusResponseSchema(BaseModel):
    """Status Response Schema."""

    data: StatusSchema
