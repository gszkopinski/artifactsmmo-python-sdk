"""Unit tests of the season_rewards endpoints (mocked, no network)."""


def test_get_all_season_rewards(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "code": "x",
                    "type": "badge",
                    "description": "x",
                    "required_points": 1,
                    "quantity": 1,
                    "member_required": True,
                    "first_only": True,
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.season_rewards.get_all_season_rewards()
    assert (message, data is not None) == ("Successfully fetched season rewards.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/season_rewards",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
