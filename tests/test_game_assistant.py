"""Unit tests of the game_assistant endpoints (mocked, no network)."""


def test_ask_game_assistant(client, respond):
    respond(
        200,
        {
            "data": {
                "answer": "x",
                "assistant": {
                    "second": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "minute": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "hour": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "day": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                },
                "paid_with_gems": True,
            }
        },
    )
    message, data = client.game_assistant.ask_game_assistant(question="x")
    assert (message, data is not None) == (
        "The assistant has answered your question.",
        True,
    )
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/game_assistant/ask",
    )
    assert client.session.request.call_args.kwargs["json"] == {"question": "x"}


def test_ask_game_assistant_error(client, respond):
    respond(451)
    assert client.game_assistant.ask_game_assistant(question="x") == (
        "Access denied, you must be a member to do that.",
        None,
    )
