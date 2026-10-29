"""GameAssistant schemas."""

from pydantic import BaseModel

from .common import RateLimitScopeSchema


class AssistantAnswerDataSchema(BaseModel):
    """AssistantAnswerDataSchema"""

    answer: str
    assistant: RateLimitScopeSchema
    paid_with_gems: bool


class AssistantAnswerSchema(BaseModel):
    """AssistantAnswerSchema"""

    data: AssistantAnswerDataSchema
