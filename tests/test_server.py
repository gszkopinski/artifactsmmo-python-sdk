"""Unit tests of the server endpoints (mocked, no network)."""


def test_get_server_details(client, respond):
    respond(
        200,
        {
            "data": {
                "version": "x",
                "server_time": "2024-01-01T00:00:00Z",
                "max_level": 1,
                "max_skill_level": 1,
                "characters_online": 1,
                "season": {
                    "name": "x",
                    "number": 1,
                    "start_date": "2024-01-01T00:00:00Z",
                    "rewards": [
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
                },
                "rate_limits": [{"type": "x", "value": "x"}],
            }
        },
    )
    message, data = client.server.get_server_details()
    assert (message, data is not None) == ("Successfully fetched status.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/")
