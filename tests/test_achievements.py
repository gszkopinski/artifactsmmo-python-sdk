"""Unit tests of the achievements endpoints (mocked, no network)."""


def test_get_all_achievements(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "description": "x",
                    "points": 1,
                    "objectives": [{"type": "combat_kill", "target": "x", "total": 1}],
                    "rewards": {"gold": 1, "items": [{"code": "x", "quantity": 1}]},
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.achievements.get_all_achievements()
    assert (message, data is not None) == ("Successfully fetched achievements.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/achievements",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_achievement(client, respond):
    respond(
        200,
        {
            "data": {
                "name": "x",
                "code": "x",
                "description": "x",
                "points": 1,
                "objectives": [{"type": "combat_kill", "target": "x", "total": 1}],
                "rewards": {"gold": 1, "items": [{"code": "x", "quantity": 1}]},
            }
        },
    )
    message, data = client.achievements.get_achievement(code="x")
    assert (message, data is not None) == ("Successfully fetched achievement.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/achievements/x",
    )


def test_get_achievement_error(client, respond):
    respond(404)
    assert client.achievements.get_achievement(code="x") == (
        "achievement not found.",
        None,
    )
