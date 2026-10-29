"""Unit tests of every endpoint: HTTP verb, path and error mapping (no network)."""

import pytest

from artifactsmmo_sdk.models.actions import SlotEnum
from artifactsmmo_sdk.models.characters import CharacterSkinEnum

N = "bob"

ENDPOINTS = {
    # id: (call, verb, path)
    "move": (lambda c: c.actions.move(N, 1, 2), "POST", f"/my/{N}/action/move"),
    "transition": (
        lambda c: c.actions.transition(N),
        "POST",
        f"/my/{N}/action/transition",
    ),
    "rest": (lambda c: c.actions.rest(N), "POST", f"/my/{N}/action/rest"),
    "fight": (lambda c: c.actions.fight(N), "POST", f"/my/{N}/action/fight"),
    "gathering": (
        lambda c: c.actions.gathering(N),
        "POST",
        f"/my/{N}/action/gathering",
    ),
    "crafting": (
        lambda c: c.actions.crafting(N, "sword", 1),
        "POST",
        f"/my/{N}/action/crafting",
    ),
    "equip": (
        lambda c: c.actions.equip_item(N, "sword", SlotEnum.WEAPON, 1),
        "POST",
        f"/my/{N}/action/equip",
    ),
    "unequip": (
        lambda c: c.actions.unequip_item(N, SlotEnum.WEAPON, 1),
        "POST",
        f"/my/{N}/action/unequip",
    ),
    "use_item": (
        lambda c: c.actions.use_item(N, "potion", 1),
        "POST",
        f"/my/{N}/action/use",
    ),
    "delete_item": (
        lambda c: c.actions.delete_item(N, "sword", 1),
        "POST",
        f"/my/{N}/action/delete",
    ),
    "recycling": (
        lambda c: c.actions.recycling(N, "sword", 1),
        "POST",
        f"/my/{N}/action/recycling",
    ),
    "deposit_bank": (
        lambda c: c.actions.deposit_bank(N, "sword", 1),
        "POST",
        f"/my/{N}/action/bank/deposit",
    ),
    "withdraw_bank": (
        lambda c: c.actions.withdraw_bank(N, "sword", 1),
        "POST",
        f"/my/{N}/action/bank/withdraw",
    ),
    "deposit_gold": (
        lambda c: c.actions.deposit_bank_gold(N, 1),
        "POST",
        f"/my/{N}/action/bank/deposit/gold",
    ),
    "withdraw_gold": (
        lambda c: c.actions.withdraw_bank_gold(N, 1),
        "POST",
        f"/my/{N}/action/bank/withdraw/gold",
    ),
    "accept_task": (
        lambda c: c.actions.accept_new_task(N),
        "POST",
        f"/my/{N}/action/task/new",
    ),
    "complete_task": (
        lambda c: c.actions.complete_task(N),
        "POST",
        f"/my/{N}/action/task/complete",
    ),
    "task_exchange": (
        lambda c: c.actions.task_exchange(N),
        "POST",
        f"/my/{N}/action/task/exchange",
    ),
    "my_characters": (lambda c: c.actions.get_my_characters(), "GET", "/my/characters"),
    "my_logs": (lambda c: c.actions.get_all_character_logs(), "GET", "/my/logs"),
    "get_character": (
        lambda c: c.characters.get_character(N),
        "GET",
        f"/characters/{N}",
    ),
    "create_character": (
        lambda c: c.characters.create_character(N, CharacterSkinEnum.MEN1),
        "POST",
        "/characters/create",
    ),
    "delete_character": (
        lambda c: c.characters.delete_character(N),
        "POST",
        "/characters/delete",
    ),
    "account_details": (
        lambda c: c.account.get_account_details(),
        "GET",
        "/my/details",
    ),
    "bank_details": (lambda c: c.account.get_bank_details(), "GET", "/my/bank"),
    "item": (lambda c: c.items.get_item("sword"), "GET", "/items/sword"),
    "monster": (lambda c: c.monsters.get_monster("pig"), "GET", "/monsters/pig"),
    "resource": (lambda c: c.resources.get_resource("tree"), "GET", "/resources/tree"),
    "map": (lambda c: c.maps.get_map(1, 2), "GET", "/maps/1/2"),
    "events": (lambda c: c.events.get_all_active_events(), "GET", "/events/active"),
}


@pytest.mark.parametrize("name", ENDPOINTS)
def test_request_shape(client, name, respond):
    call, verb, path = ENDPOINTS[name]
    respond(500)
    message, data = call(client)
    assert data is None
    assert message.startswith("Unknown error")
    assert client.session.request.call_args.args == (verb, f"http://api.test{path}")


@pytest.mark.parametrize("name", [n for n in ENDPOINTS if ENDPOINTS[n][1] == "POST"])
def test_actions_report_cooldown(client, name, respond):
    respond(499)
    message, data = ENDPOINTS[name][0](client)
    assert data is None
    assert "cooldown" in message.lower()


def test_move_body(client, respond):
    respond(500)
    client.actions.move(N, 1, 2)
    assert client.session.request.call_args.kwargs["json"] == {
        "x": 1,
        "y": 2,
        "map_id": 0,
    }


def test_pagination_params(client, respond):
    respond(500)
    client.monsters.get_all_monsters("", 0, 0, page=2, size=10)
    assert client.session.request.call_args.kwargs["params"] == {"page": 2, "size": 10}


def test_get_item_404(client, respond):
    respond(404)
    assert client.items.get_item("x") == ("Item not found.", None)
