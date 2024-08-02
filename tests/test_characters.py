"""Test characters."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


artifacts_client = ArtifactsClient()


def test_get_character():
    """Tests."""
    result = artifacts_client.characters.get_character(
        name="billy1",
    )

    assert result
    ic(result)
