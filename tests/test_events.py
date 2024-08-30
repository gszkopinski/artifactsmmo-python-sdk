"""Test events."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


artifacts_client = ArtifactsClient()


def test_get_all_events():
    """Test."""
    error, events = artifacts_client.events.get_all_events()
    if not events:
        raise Exception(error)

    for event in events.data:
        ic(event)
    assert events
