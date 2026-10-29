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


def test_get_ge_orders(client, respond):
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
    message, data = client.grand_exchange.get_ge_orders()
    assert (message, data is not None) == ("Successfully fetched GE orders.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/grandexchange/orders",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_ge_order(client, respond):
    respond(
        200,
        {
            "data": {
                "id": "x",
                "type": "sell",
                "account": "x",
                "code": "x",
                "quantity": 1,
                "price": 1,
                "created_at": "2024-01-01T00:00:00Z",
            }
        },
    )
    message, data = client.grand_exchange.get_ge_order(id="x")
    assert (message, data is not None) == ("Successfully fetched GE order.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/grandexchange/orders/x",
    )


def test_get_ge_order_error(client, respond):
    respond(404)
    assert client.grand_exchange.get_ge_order(id="x") == ("GE order not found.", None)
