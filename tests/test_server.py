"""Test Server."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


artifacts_client = ArtifactsClient()


def test_status():
    """Tests."""
    result = artifacts_client.server.status()

    assert result
    ic(result)
