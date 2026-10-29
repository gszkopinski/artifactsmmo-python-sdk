"""Unit tests of the grand_exchange endpoints (mocked, no network)."""


def test_get_ge_history(client, respond):
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
    message, data = client.grand_exchange.get_ge_history(code="x")
    assert (message, data is not None) == ("Successfully fetched item history.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/grandexchange/history/x",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_ge_history_error(client, respond):
    respond(404)
    assert client.grand_exchange.get_ge_history(code="x") == (
        "item history not found.",
        None,
    )
