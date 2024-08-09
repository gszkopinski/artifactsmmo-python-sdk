"""Test characters."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


artifacts_client = ArtifactsClient()


def test_get_character():
    """Tests."""
    error, result = artifacts_client.characters.get_character(
        name="billy1",
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
