"""Unit tests of the items endpoints (mocked, no network)."""


def test_get_all_items(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "level": 1,
                    "type": "x",
                    "subtype": "x",
                    "description": "x",
                    "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                    "effects": [{"code": "x", "value": 1, "description": "x"}],
                    "craft": {
                        "skill": "weaponcrafting",
                        "level": 1,
                        "items": [{"code": "x", "quantity": 1}],
                        "quantity": 1,
                    },
                    "tradeable": True,
                    "recyclable": True,
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.items.get_all_items()
    assert (message, data is not None) == ("Successfully fetched items.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/items")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
