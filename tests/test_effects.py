"""Unit tests of the effects endpoints (mocked, no network)."""


def test_get_all_effects(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "description": "x",
                    "type": "equipment",
                    "subtype": "stat",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.effects.get_all_effects()
    assert (message, data is not None) == ("Successfully fetched effects.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/effects")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_effect(client, respond):
    respond(
        200,
        {
            "data": {
                "name": "x",
                "code": "x",
                "description": "x",
                "type": "equipment",
                "subtype": "stat",
            }
        },
    )
    message, data = client.effects.get_effect(code="x")
    assert (message, data is not None) == ("Successfully fetched effect.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/effects/x")


def test_get_effect_error(client, respond):
    respond(404)
    assert client.effects.get_effect(code="x") == ("effect not found.", None)
