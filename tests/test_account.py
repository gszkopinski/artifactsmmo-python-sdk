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
