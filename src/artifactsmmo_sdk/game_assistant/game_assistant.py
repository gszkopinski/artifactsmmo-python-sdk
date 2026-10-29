"""GameAssistant."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.game_assistant import (
    AssistantAnswerSchema,
)


class GameAssistant(BaseModule):
    """GameAssistant."""

    def ask_game_assistant(
        self,
        question: Annotated[str, Field(description="Your question")],
        pay_with_gems: Annotated[
            bool | None,
            Field(description="Spend 1 gem if no free member question is available."),
        ] = None,
    ) -> tuple[str, AssistantAnswerSchema | None]:
        """Ask the game assistant a question about game mechanics or public API usage.
        An active membership is required. Members receive a limited number of free
        questions per day. When no free question is available, the request can spend
        1 gem with pay_with_gems=true."""
        return self._request(
            "POST",
            "/game_assistant/ask",
            AssistantAnswerSchema,
            "The assistant has answered your question.",
            {
                451: "Access denied, you must be a member to do that.",
                563: "Insufficient gems.",
                570: "You have reached the daily limit for assistant questions. Try again tomorrow.",
            },
            json={
                "question": question,
                "pay_with_gems": pay_with_gems,
            },
        )
