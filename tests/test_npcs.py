"""Unit tests of the npcs endpoints (mocked, no network)."""


def test_get_all_npcs(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "description": "x",
                    "type": "merchant",
                    "items": [
                        {"code": "x", "currency": "x", "buy_price": 1, "sell_price": 1}
                    ],
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.npcs.get_all_npcs()
    assert (message, data is not None) == ("Successfully fetched NPCs.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/npcs/details",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
