"""Test Maps."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


artifacts_client = ArtifactsClient()


def test_get_map():
    """Tests."""
    result = artifacts_client.maps.get_map(
        x=-1,
        y=0,
    )

    assert result
    ic(result)


def test_get_all_maps():
    """Tests."""
    result = artifacts_client.maps.get_all_maps(
        content_code="ogre",
        content_type="monster",
    )

    assert result
    ic(result)
