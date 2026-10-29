"""Unit tests of the monsters endpoints (mocked, no network)."""


def test_get_all_monsters(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "level": 1,
                    "type": "normal",
                    "hp": 1,
                    "attack_fire": 1,
                    "attack_earth": 1,
                    "attack_water": 1,
                    "attack_air": 1,
                    "res_fire": 1,
                    "res_earth": 1,
                    "res_water": 1,
                    "res_air": 1,
                    "critical_strike": 1,
                    "initiative": 1,
                    "effects": [{"code": "x", "value": 1, "description": "x"}],
                    "min_gold": 1,
                    "max_gold": 1,
                    "drops": [
                        {"code": "x", "rate": 1, "min_quantity": 1, "max_quantity": 1}
                    ],
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.monsters.get_all_monsters()
    assert (message, data is not None) == ("Successfully fetched monsters.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/monsters")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_monster(client, respond):
    respond(
        200,
        {
            "data": {
                "name": "x",
                "code": "x",
                "level": 1,
                "type": "normal",
                "hp": 1,
                "attack_fire": 1,
                "attack_earth": 1,
                "attack_water": 1,
                "attack_air": 1,
                "res_fire": 1,
                "res_earth": 1,
                "res_water": 1,
                "res_air": 1,
                "critical_strike": 1,
                "initiative": 1,
                "effects": [{"code": "x", "value": 1, "description": "x"}],
                "min_gold": 1,
                "max_gold": 1,
                "drops": [
                    {"code": "x", "rate": 1, "min_quantity": 1, "max_quantity": 1}
                ],
            }
        },
    )
    message, data = client.monsters.get_monster(code="x")
    assert (message, data is not None) == ("Successfully fetched monster.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/monsters/x",
    )


def test_get_monster_error(client, respond):
    respond(404)
    assert client.monsters.get_monster(code="x") == ("monster not found.", None)
