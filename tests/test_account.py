"""Unit tests of the account endpoints (mocked, no network)."""


def test_get_bank_details(client, respond):
    respond(
        200,
        {"data": {"slots": 1, "expansions": 1, "next_expansion_cost": 1, "gold": 1}},
    )
    message, data = client.account.get_bank_details()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/my/bank")


def test_get_bank_items(client, respond):
    respond(
        200,
        {
            "data": [{"code": "x", "quantity": 1}],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.account.get_bank_items()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/bank/items",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_ge_sell_orders(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "id": "x",
                    "type": "sell",
                    "account": "x",
                    "code": "x",
                    "quantity": 1,
                    "price": 1,
                    "created_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.account.get_ge_sell_orders()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/grandexchange/orders",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_ge_sell_history(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "order_id": "x",
                    "seller": "x",
                    "buyer": "x",
                    "code": "x",
                    "quantity": 1,
                    "price": 1,
                    "sold_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.account.get_ge_sell_history()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/grandexchange/history",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_account_details(client, respond):
    respond(
        200,
        {
            "data": {
                "username": "x",
                "email": "a@b.co",
                "member": True,
                "member_expiration": "2024-01-01T00:00:00Z",
                "status": "standard",
                "badges": ["x"],
                "skins": ["x"],
                "gems": 1,
                "member_token": 1,
                "achievements_points": 1,
                "banned": True,
                "ban_reason": "x",
            }
        },
    )
    message, data = client.account.get_account_details()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/details",
    )


def test_get_pending_items(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "id": "x",
                    "account": "x",
                    "source": "achievement",
                    "source_id": "x",
                    "description": "x",
                    "gold": 1,
                    "items": [{"code": "x", "quantity": 1}],
                    "created_at": "2024-01-01T00:00:00Z",
                    "claimed_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.account.get_pending_items()
    assert (message, data is not None) == ("Successfully fetched pending items.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/pending_items",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
