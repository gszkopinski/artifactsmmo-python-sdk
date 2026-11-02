"""Unit tests of the seasonal offerings endpoints (mocked, no network)."""

OFFERING = {
    "id": "x",
    "category": "combat",
    "type": "monster",
    "level_min": 1,
    "level_max": 5,
    "requirement": {"code": "x", "quantity": 1},
    "favor": {"target_type": "monster", "target_code": "x"},
}
DAILY = {
    "date": "2024-01-01",
    "expires_at": "2024-01-02T00:00:00Z",
    "skills": ["mining", "cooking"],
    "offerings": [OFFERING],
}
COOLDOWN = {
    "total_seconds": 1,
    "remaining_seconds": 1,
    "started_at": "2024-01-01T00:00:00Z",
    "expiration": "2024-01-01T00:00:00Z",
    "reason": "offering",
}


def character() -> dict:
    """Minimal CharacterSchema payload."""
    skills = [
        f"{s}_{k}"
        for s in (
            "mining",
            "woodcutting",
            "fishing",
            "weaponcrafting",
            "gearcrafting",
            "jewelrycrafting",
            "cooking",
            "alchemy",
        )
        for k in ("level", "xp", "max_xp")
    ]
    ints = [
        "level", "xp", "max_xp", "gold", "speed", "hp", "max_hp", "haste",
        "critical_strike", "wisdom", "prospecting", "initiative", "threat", "dmg",
        "x", "y", "map_id", "cooldown", "task_progress", "task_total",
        "inventory_max_items", "utility1_slot_quantity", "utility2_slot_quantity",
    ]  # fmt: skip
    for element in ("fire", "earth", "water", "air"):
        ints += [f"attack_{element}", f"dmg_{element}", f"res_{element}"]
    slots = [
        "weapon", "rune", "shield", "helmet", "body_armor", "leg_armor", "boots",
        "ring1", "ring2", "amulet", "artifact1", "artifact2", "artifact3",
        "utility1", "utility2", "bag",
    ]  # fmt: skip
    data: dict = dict.fromkeys(skills + ints, 1)
    data.update(dict.fromkeys(["name", "account", "skin", "task", "task_type"], "x"))
    data.update({f"{slot}_slot": "x" for slot in slots})
    data["layer"] = "overworld"
    return data


def test_get_daily_seasonal_offerings(client, respond):
    respond(200, {"data": DAILY})
    message, data = client.seasonal_offerings.get_daily_seasonal_offerings()
    assert (message, data is not None) == (
        "Successfully fetched seasonal offerings.",
        True,
    )
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/seasonal_offerings",
    )


def test_get_daily_seasonal_offerings_error(client, respond):
    respond(575)
    assert client.seasonal_offerings.get_daily_seasonal_offerings() == (
        "This seasonal offering is not available.",
        None,
    )


def test_get_character_seasonal_offerings(client, respond):
    respond(
        200,
        {
            "data": {
                **DAILY,
                "selected_offerings": [
                    {
                        "offering_id": "x",
                        "category": "combat",
                        "status": "accepted",
                        "accepted_at": "2024-01-01T00:00:00Z",
                        "requirement": {"code": "x", "quantity": 1},
                        "favor": {"target_type": "monster", "target_code": "x"},
                        "expires_at": "2024-01-02T00:00:00Z",
                    }
                ],
                "completed_categories": ["mining"],
                "active_favors": [{"target_type": "monster", "target_code": "x"}],
            }
        },
    )
    message, data = client.actions.get_character_seasonal_offerings(name="bob")
    assert (message, data is not None) == (
        "Successfully fetched seasonal offerings.",
        True,
    )
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/bob/offerings",
    )


def test_get_character_seasonal_offerings_error(client, respond):
    respond(498)
    assert client.actions.get_character_seasonal_offerings(name="bob") == (
        "Character not found.",
        None,
    )


def test_accept_seasonal_offering(client, respond):
    respond(
        200,
        {
            "data": {
                "cooldown": COOLDOWN,
                "offering": OFFERING,
                "favor_expires_at": "2024-01-02T00:00:00Z",
                "character": character(),
            }
        },
    )
    message, data = client.actions.accept_seasonal_offering(name="bob", offering_id="x")
    assert (message, data is not None) == ("The offering has been accepted.", True)
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/my/bob/action/offering/accept",
    )
    assert client.session.request.call_args.kwargs["json"] == {"offering_id": "x"}


def test_accept_seasonal_offering_error(client, respond):
    respond(576)
    assert client.actions.accept_seasonal_offering(name="bob", offering_id="x") == (
        "The character has already selected an offering in this category today.",
        None,
    )


def test_complete_seasonal_offering(client, respond):
    respond(
        200,
        {
            "data": {
                "cooldown": COOLDOWN,
                "offering": OFFERING,
                "reward": {"category": "combat", "xp": 10},
                "favor_expires_at": "2024-01-02T00:00:00Z",
                "character": character(),
            }
        },
    )
    message, data = client.actions.complete_seasonal_offering(
        name="bob", offering_id="x"
    )
    assert (message, data is not None) == ("The offering has been completed.", True)
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/my/bob/action/offering",
    )
    assert client.session.request.call_args.kwargs["json"] == {"offering_id": "x"}


def test_complete_seasonal_offering_error(client, respond):
    respond(577)
    assert client.actions.complete_seasonal_offering(name="bob", offering_id="x") == (
        "The character must accept this seasonal offering first.",
        None,
    )
