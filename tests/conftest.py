"""Shared fixtures for unit tests."""

import pytest
import requests

from artifactsmmo_sdk import ArtifactsClient


@pytest.fixture
def client(mocker) -> ArtifactsClient:
    """Client whose session never touches the network."""
    client = ArtifactsClient(token="token", api_url="http://api.test")
    mocker.patch.object(client.session, "request")
    return client


@pytest.fixture
def respond(client, mocker):
    """Make the next API call answer with `status` and a JSON `payload`."""

    def _respond(status: int = 200, payload: dict | None = None) -> None:
        response = mocker.MagicMock(status_code=status)
        response.json.return_value = payload
        if status >= 400:
            response.raise_for_status.side_effect = requests.exceptions.HTTPError(
                response=response
            )
        client.session.request.return_value = response

    return _respond
