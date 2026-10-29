"""Unit tests of the leaderboard endpoints (mocked, no network)."""


def test_get_characters_leaderboard(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "position": 1,
                    "name": "x",
                    "account": "x",
                    "member": True,
                    "skin": "x",
                    "level": 1,
                    "total_xp": 1,
                    "mining_level": 1,
                    "mining_total_xp": 1,
                    "woodcutting_level": 1,
                    "woodcutting_total_xp": 1,
                    "fishing_level": 1,
                    "fishing_total_xp": 1,
                    "weaponcrafting_level": 1,
                    "weaponcrafting_total_xp": 1,
                    "gearcrafting_level": 1,
                    "gearcrafting_total_xp": 1,
                    "jewelrycrafting_level": 1,
                    "jewelrycrafting_total_xp": 1,
                    "cooking_level": 1,
                    "cooking_total_xp": 1,
                    "alchemy_level": 1,
                    "alchemy_total_xp": 1,
                    "gold": 1,
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.leaderboard.get_characters_leaderboard()
    assert (message, data is not None) == ("Successfully fetched leaderboard.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/leaderboard/characters",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_accounts_leaderboard(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "position": 1,
                    "account": "x",
                    "member": True,
                    "achievements_points": 1,
                    "completed_at": "2024-01-01T00:00:00Z",
                    "gold": 1,
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.leaderboard.get_accounts_leaderboard()
    assert (message, data is not None) == ("Successfully fetched leaderboard.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/leaderboard/accounts",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
