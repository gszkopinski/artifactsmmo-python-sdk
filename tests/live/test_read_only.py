"""Read-only smoke tests against the real API (no character is created or moved)."""

import pytest

from artifactsmmo_sdk import ArtifactsClient


@pytest.fixture(scope="module")
def client() -> ArtifactsClient:
    return ArtifactsClient()


@pytest.mark.parametrize(
    "call",
    [
        lambda c: c.server.get_server_details(),
        lambda c: c.items.get_all_items(size=5),
        lambda c: c.monsters.get_all_monsters(size=5),
        lambda c: c.resources.get_all_resources(size=5),
        lambda c: c.maps.get_all_maps(size=5),
        lambda c: c.events.get_all_active_events(size=5),
        lambda c: c.effects.get_all_effects(size=5),
        lambda c: c.npcs.get_all_npcs(size=5),
        lambda c: c.tasks.get_all_tasks(size=5),
        lambda c: c.achievements.get_all_achievements(size=5),
        lambda c: c.account.get_account_details(),
        lambda c: c.account.get_bank_details(),
    ],
)
def test_read_only_endpoints_validate_against_models(client, call):
    message, data = call(client)
    assert data is not None, message
