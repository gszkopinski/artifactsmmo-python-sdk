"""Unit tests of the characters endpoints (mocked, no network)."""


def test_create_character(client, respond):
    respond(
        200,
        {
            "data": {
                "name": "x",
                "account": "x",
                "skin": "x",
                "level": 1,
                "xp": 1,
                "max_xp": 1,
                "gold": 1,
                "speed": 1,
                "mining_level": 1,
                "mining_xp": 1,
                "mining_max_xp": 1,
                "woodcutting_level": 1,
                "woodcutting_xp": 1,
                "woodcutting_max_xp": 1,
                "fishing_level": 1,
                "fishing_xp": 1,
                "fishing_max_xp": 1,
                "weaponcrafting_level": 1,
                "weaponcrafting_xp": 1,
                "weaponcrafting_max_xp": 1,
                "gearcrafting_level": 1,
                "gearcrafting_xp": 1,
                "gearcrafting_max_xp": 1,
                "jewelrycrafting_level": 1,
                "jewelrycrafting_xp": 1,
                "jewelrycrafting_max_xp": 1,
                "cooking_level": 1,
                "cooking_xp": 1,
                "cooking_max_xp": 1,
                "alchemy_level": 1,
                "alchemy_xp": 1,
                "alchemy_max_xp": 1,
                "hp": 1,
                "max_hp": 1,
                "haste": 1,
                "critical_strike": 1,
                "wisdom": 1,
                "prospecting": 1,
                "initiative": 1,
                "threat": 1,
                "attack_fire": 1,
                "attack_earth": 1,
                "attack_water": 1,
                "attack_air": 1,
                "dmg": 1,
                "dmg_fire": 1,
                "dmg_earth": 1,
                "dmg_water": 1,
                "dmg_air": 1,
                "res_fire": 1,
                "res_earth": 1,
                "res_water": 1,
                "res_air": 1,
                "effects": [{"code": "x", "value": 1}],
                "x": 1,
                "y": 1,
                "layer": "interior",
                "map_id": 1,
                "cooldown": 1,
                "cooldown_expiration": "2024-01-01T00:00:00Z",
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
                "bag_slot": "x",
                "task": "x",
                "task_type": "x",
                "task_progress": 1,
                "task_total": 1,
                "inventory_max_items": 1,
                "inventory": [{"slot": 1, "code": "x", "quantity": 1}],
            }
        },
    )
    message, data = client.characters.create_character(name="x", skin="x")
    assert (message, data is not None) == ("Successfully created character.", True)
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/characters/create",
    )
    assert client.session.request.call_args.kwargs["json"] == {"name": "x", "skin": "x"}


def test_create_character_error(client, respond):
    respond(404)
    assert client.characters.create_character(name="x", skin="x") == (
        "Skin not found.",
        None,
    )


def test_delete_character(client, respond):
    respond(
        200,
        {
            "data": {
                "name": "x",
                "account": "x",
                "skin": "x",
                "level": 1,
                "xp": 1,
                "max_xp": 1,
                "gold": 1,
                "speed": 1,
                "mining_level": 1,
                "mining_xp": 1,
                "mining_max_xp": 1,
                "woodcutting_level": 1,
                "woodcutting_xp": 1,
                "woodcutting_max_xp": 1,
                "fishing_level": 1,
                "fishing_xp": 1,
                "fishing_max_xp": 1,
                "weaponcrafting_level": 1,
                "weaponcrafting_xp": 1,
                "weaponcrafting_max_xp": 1,
                "gearcrafting_level": 1,
                "gearcrafting_xp": 1,
                "gearcrafting_max_xp": 1,
                "jewelrycrafting_level": 1,
                "jewelrycrafting_xp": 1,
                "jewelrycrafting_max_xp": 1,
                "cooking_level": 1,
                "cooking_xp": 1,
                "cooking_max_xp": 1,
                "alchemy_level": 1,
                "alchemy_xp": 1,
                "alchemy_max_xp": 1,
                "hp": 1,
                "max_hp": 1,
                "haste": 1,
                "critical_strike": 1,
                "wisdom": 1,
                "prospecting": 1,
                "initiative": 1,
                "threat": 1,
                "attack_fire": 1,
                "attack_earth": 1,
                "attack_water": 1,
                "attack_air": 1,
                "dmg": 1,
                "dmg_fire": 1,
                "dmg_earth": 1,
                "dmg_water": 1,
                "dmg_air": 1,
                "res_fire": 1,
                "res_earth": 1,
                "res_water": 1,
                "res_air": 1,
                "effects": [{"code": "x", "value": 1}],
                "x": 1,
                "y": 1,
                "layer": "interior",
                "map_id": 1,
                "cooldown": 1,
                "cooldown_expiration": "2024-01-01T00:00:00Z",
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
                "bag_slot": "x",
                "task": "x",
                "task_type": "x",
                "task_progress": 1,
                "task_total": 1,
                "inventory_max_items": 1,
                "inventory": [{"slot": 1, "code": "x", "quantity": 1}],
            }
        },
    )
    message, data = client.characters.delete_character(name="x")
    assert (message, data is not None) == ("Successfully deleted character.", True)
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/characters/delete",
    )
    assert client.session.request.call_args.kwargs["json"] == {"name": "x"}


def test_delete_character_error(client, respond):
    respond(498)
    assert client.characters.delete_character(name="x") == (
        "Character not found.",
        None,
    )


def test_get_character_stats(client, respond):
    respond(
        200,
        {
            "data": {
                "monsters_killed": {"k": 1},
                "resources_gathered": {"k": 1},
                "items_crafted": {"k": 1},
                "action_counts": {"k": 1},
                "deaths": 1,
            }
        },
    )
    message, data = client.characters.get_character_stats(name="bob")
    assert (message, data is not None) == (
        "Successfully fetched character stats.",
        True,
    )
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/characters/bob/stats",
    )


def test_get_character_stats_error(client, respond):
    respond(404)
    assert client.characters.get_character_stats(name="bob") == (
        "character stats not found.",
        None,
    )


def test_get_active_characters(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "account": "x",
                    "skin": "x",
                    "x": 1,
                    "y": 1,
                    "layer": "interior",
                    "map_id": 1,
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.characters.get_active_characters()
    assert (message, data is not None) == (
        "Successfully fetched active characters.",
        True,
    )
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/characters/active",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
