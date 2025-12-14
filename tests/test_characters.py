"""Test Characters."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient
from artifactsmmo_sdk.models.characters import CharacterSkinEnum


artifacts_client = ArtifactsClient()


def test_create_character():
    """Tests."""
    error, result = artifacts_client.characters.create_character(
        name="billy2",
        skin=CharacterSkinEnum.MEN1,
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)


def test_get_character():
    """Tests."""
    error, result = artifacts_client.characters.get_character(
        name="billy2",
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)


def test_get_all_characters():
    """Tests."""
    error, result = artifacts_client.characters.get_all_characters()

    if not result:
        print(error)

    else:
        assert result
        ic(result)


def test_delete_character():
    """Tests."""
    error, result = artifacts_client.characters.delete_character(
        name="billy2",
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)
