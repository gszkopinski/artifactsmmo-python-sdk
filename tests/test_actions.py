"""Test characters."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


artifacts_client = ArtifactsClient()


def test_action_move():
    """Tests."""
    result = artifacts_client.actions.move(
        name="billy1",
        x=0,
        y=1,
    )

    assert result
    ic(result)


def test_action_move_back():
    """Tests."""
    result = artifacts_client.actions.move(
        name="billy1",
        x=0,
        y=0,
    )

    assert result
    ic(result)


def test_unequip_item():
    """Tests."""
    result = artifacts_client.actions.unequip_item(
        name="billy1",
        slot="weapon",
    )

    assert result
    ic(result)


def test_equip_item():
    """Tests."""
    result = artifacts_client.actions.equip_item(
        name="billy1",
        code="wooden_stick",
        slot="weapon",
    )

    assert result
    ic(result)


def test_get_character_logs():
    """Tests."""
    result = artifacts_client.actions.get_character_logs(name="billy1")

    assert result
    ic(result)


def test_gathering():
    """Tests."""
    result = artifacts_client.actions.gathering(name="billy1")

    assert result
    ic(result)
