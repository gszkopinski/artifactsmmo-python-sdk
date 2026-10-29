"""Unit tests of the gems_shop endpoints (mocked, no network)."""


def test_get_catalog(client, respond):
    respond(
        200,
        {
            "data": {
                "skins": [{"code": "x", "name": "x", "description": "x", "price": 1}],
                "spawn_events": [
                    {
                        "code": "x",
                        "name": "x",
                        "content_type": "monster",
                        "content_code": "x",
                        "duration": 1,
                        "price": 1,
                    }
                ],
                "subscriptions": [
                    {"code": "x", "name": "x", "duration_days": 1, "price": 1}
                ],
                "custom_designs": [
                    {
                        "code": "x",
                        "name": "x",
                        "description": "x",
                        "price": 1,
                        "category": "npc",
                        "unique_to_account": True,
                    }
                ],
            }
        },
    )
    message, data = client.gems_shop.get_catalog()
    assert (message, data is not None) == (
        "Successfully fetched gems shop catalog.",
        True,
    )
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/gems_shop/",
    )


def test_buy_skin(client, respond):
    respond(200, {"data": {"skins": ["x"], "skin": "x", "gems": 1}})
    message, data = client.gems_shop.buy_skin(code="x")
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/gems_shop/skin",
    )
    assert client.session.request.call_args.kwargs["json"] == {"code": "x"}


def test_buy_skin_error(client, respond):
    respond(404)
    assert client.gems_shop.buy_skin(code="x") == ("Skin not found.", None)
