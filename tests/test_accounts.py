"""Unit tests of the accounts endpoints (mocked, no network)."""


def test_get_account_achievements(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "description": "x",
                    "points": 1,
                    "objectives": [
                        {
                            "type": "combat_kill",
                            "target": "x",
                            "progress": 1,
                            "total": 1,
                        }
                    ],
                    "rewards": {"gold": 1, "items": [{"code": "x", "quantity": 1}]},
                    "completed_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.accounts.get_account_achievements(account="x")
    assert (message, data is not None) == ("Successfully fetched achievements.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/accounts/x/achievements",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_account_achievements_error(client, respond):
    respond(404)
    assert client.accounts.get_account_achievements(account="x") == (
        "Account not found.",
        None,
    )


def test_get_account_characters(client, respond):
    respond(
        200,
        {
            "data": [
                {
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
            ]
        },
    )
    message, data = client.accounts.get_account_characters(account="x")
    assert (message, data is not None) == (
        "Successfully fetched account characters.",
        True,
    )
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/accounts/x/characters",
    )


def test_create_account(client, respond):
    respond(200, {"message": "x"})
    message, data = client.accounts.create_account(
        username="x", password="x", email="a@b.co"
    )
    assert (message, data is not None) == ("Account created successfully.", True)
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/accounts/create",
    )
    assert client.session.request.call_args.kwargs["json"] == {
        "username": "x",
        "password": "x",
        "email": "a@b.co",
    }


def test_create_account_error(client, respond):
    respond(456)
    assert client.accounts.create_account(
        username="x", password="x", email="a@b.co"
    ) == ("This username is already taken.", None)


def test_forgot_password(client, respond):
    respond(200, {"message": "x"})
    message, data = client.accounts.forgot_password(email="a@b.co")
    assert (message, data is not None) == (
        "If this email address is associated with an account, a reset link has been sent.",
        True,
    )
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/accounts/forgot_password",
    )
    assert client.session.request.call_args.kwargs["json"] == {"email": "a@b.co"}


def test_forgot_password_error(client, respond):
    respond(422)
    assert client.accounts.forgot_password(email="a@b.co") == (
        "Request could not be processed due to an invalid payload.",
        None,
    )


def test_reset_password(client, respond):
    respond(200, {"message": "x"})
    message, data = client.accounts.reset_password(token="x", new_password="x")
    assert (message, data is not None) == (
        "Password has been successfully reset.",
        True,
    )
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/accounts/reset_password",
    )
    assert client.session.request.call_args.kwargs["json"] == {
        "token": "x",
        "new_password": "x",
    }


def test_reset_password_error(client, respond):
    respond(560)
    assert client.accounts.reset_password(token="x", new_password="x") == (
        "The password reset token is invalid.",
        None,
    )
