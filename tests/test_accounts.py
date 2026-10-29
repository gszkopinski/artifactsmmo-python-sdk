"""Unit tests of the accounts endpoints (mocked, no network)."""


def test_get_account_achievements(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "description": "x",
                    "points": 1,
                    "objectives": [
                        {
                            "type": "combat_kill",
                            "target": "x",
                            "progress": 1,
                            "total": 1,
                        }
                    ],
                    "rewards": {"gold": 1, "items": [{"code": "x", "quantity": 1}]},
                    "completed_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.accounts.get_account_achievements(account="x")
    assert (message, data is not None) == ("Successfully fetched achievements.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/accounts/x/achievements",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_account_achievements_error(client, respond):
    respond(404)
    assert client.accounts.get_account_achievements(account="x") == (
        "Account not found.",
        None,
    )
