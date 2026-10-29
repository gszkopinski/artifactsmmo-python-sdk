"""Unit tests of the token endpoint (HTTP Basic auth, outside the shared session)."""

import pytest
import requests

from artifactsmmo_sdk.token import Token


@pytest.fixture
def post(mocker):
    return mocker.patch("artifactsmmo_sdk.token.token.requests.post")


def _response(mocker, status, payload=None):
    response = mocker.MagicMock(status_code=status)
    response.json.return_value = payload
    if status >= 400:
        response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            response=response
        )
    return response


def test_generate_token(mocker, post):
    post.return_value = _response(mocker, 200, {"token": "abc"})
    message, data = Token("http://api.test", requests.Session()).generate_token(
        "bob", "secret"
    )
    assert (message, data.token) == ("Token generated successfully", "abc")
    assert post.call_args.kwargs["url"] == "http://api.test/token"
    assert post.call_args.kwargs["headers"]["Authorization"] == "Basic Ym9iOnNlY3JldA=="


@pytest.mark.parametrize(
    ("status", "message"),
    [
        (422, "Request could not be processed due to an invalid payload."),
        (455, "Failed to generate token."),
    ],
)
def test_generate_token_errors(mocker, post, status, message):
    post.return_value = _response(mocker, status)
    result = Token("http://api.test", requests.Session()).generate_token("bob", "x")
    assert result == (message, None)
