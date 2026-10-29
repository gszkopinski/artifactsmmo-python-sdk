"""Unit tests of the simulation endpoints (mocked, no network)."""


def test_fight_simulation(client, respond):
    respond(
        200,
        {
            "data": {
                "results": [
                    {
                        "result": "x",
                        "turns": 1,
                        "logs": ["x"],
                        "character_results": [{}],
                    }
                ],
                "wins": 1,
                "losses": 1,
                "winrate": 1.0,
            }
        },
    )
    message, data = client.simulation.fight_simulation(
        characters=[
            {
                "level": 1,
                "weapon_slot": "x",
                "rune_slot": "x",
                "shield_slot": "x",
                "helmet_slot": "x",
                "body_armor_slot": "x",
                "leg_armor_slot": "x",
                "boots_slot": "x",
                "ring1_slot": "x",
                "ring2_slot": "x",
                "amulet_slot": "x",
                "artifact1_slot": "x",
                "artifact2_slot": "x",
                "artifact3_slot": "x",
                "utility1_slot": "x",
                "utility1_slot_quantity": 1,
                "utility2_slot": "x",
                "utility2_slot_quantity": 1,
            }
        ],
        monster="x",
        iterations=1,
    )
    assert (message, data is not None) == (
        "Combat simulation completed successfully.",
        True,
    )
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/simulation/fight",
    )
    assert client.session.request.call_args.kwargs["json"] == {
        "characters": [
            {
                "level": 1,
                "weapon_slot": "x",
                "rune_slot": "x",
                "shield_slot": "x",
                "helmet_slot": "x",
                "body_armor_slot": "x",
                "leg_armor_slot": "x",
                "boots_slot": "x",
                "ring1_slot": "x",
                "ring2_slot": "x",
                "amulet_slot": "x",
                "artifact1_slot": "x",
                "artifact2_slot": "x",
                "artifact3_slot": "x",
                "utility1_slot": "x",
                "utility1_slot_quantity": 1,
                "utility2_slot": "x",
                "utility2_slot_quantity": 1,
            }
        ],
        "monster": "x",
        "iterations": 1,
    }


def test_fight_simulation_error(client, respond):
    respond(404)
    assert client.simulation.fight_simulation(
        characters=[
            {
                "level": 1,
                "weapon_slot": "x",
                "rune_slot": "x",
                "shield_slot": "x",
                "helmet_slot": "x",
                "body_armor_slot": "x",
                "leg_armor_slot": "x",
                "boots_slot": "x",
                "ring1_slot": "x",
                "ring2_slot": "x",
                "amulet_slot": "x",
                "artifact1_slot": "x",
                "artifact2_slot": "x",
                "artifact3_slot": "x",
                "utility1_slot": "x",
                "utility1_slot_quantity": 1,
                "utility2_slot": "x",
                "utility2_slot_quantity": 1,
            }
        ],
        monster="x",
        iterations=1,
    ) == ("Monster or item not found.", None)
