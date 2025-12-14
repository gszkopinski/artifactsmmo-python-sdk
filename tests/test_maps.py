"""Test Maps."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient
from artifactsmmo_sdk.models.maps import MapContentTypeSchema


artifacts_client = ArtifactsClient()


def test_get_map():
    """Tests."""
    error, result = artifacts_client.maps.get_map(
        x=-1,
        y=0,
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)


def test_get_all_maps():
    """Tests."""
    error, result = artifacts_client.maps.get_all_maps(
        content_code="ogre",
        content_type=MapContentTypeSchema.MONSTER,
    )

    if not result:
        print(error)

    else:
        assert result
        ic(result)
