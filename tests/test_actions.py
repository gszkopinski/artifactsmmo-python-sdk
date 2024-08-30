"""Test characters."""

from time import sleep
from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


artifacts_client = ArtifactsClient()


def get_character_name():
    """Get Character."""
    error, character = artifacts_client.characters.get_character(
        name="billy1",
    )
    if not character:
        raise Exception(error)

    return character.data.name


def test_action_move():
    """Tests."""
    error, result = artifacts_client.actions.move(
        name=get_character_name(),
        x=0,
        y=1,
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)
        sleep(result.data.cooldown.total_seconds)


def test_action_move_back():
    """Tests."""
    error, result = artifacts_client.actions.move(
        name=get_character_name(),
        x=0,
        y=0,
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)
        sleep(result.data.cooldown.total_seconds)


def test_unequip_item():
    """Tests."""
    error, result = artifacts_client.actions.unequip_item(
        name=get_character_name(),
        slot="weapon",
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)
        sleep(result.data.cooldown.total_seconds)


def test_equip_item():
    """Tests."""
    error, result = artifacts_client.actions.equip_item(
        name=get_character_name(),
        code="wooden_stick",
        slot="weapon",
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)
        sleep(result.data.cooldown.total_seconds)


def test_get_all_character_logs():
    """Tests."""
    error, result = artifacts_client.actions.get_all_character_logs()

    if not result:
        print(error)

    else:
        assert result
        ic(result)
        sleep(1)


def test_gathering():
    """Tests."""
    error, result = artifacts_client.actions.gathering(name=get_character_name())

    if not result:
        print(error)

    else:
        assert result
        ic(result)
        sleep(result.data.cooldown.total_seconds)
