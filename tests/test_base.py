"""Unit tests for the shared request plumbing and the client."""

from enum import Enum

import pytest
from pydantic import BaseModel

from artifactsmmo_sdk import ArtifactsClient
from artifactsmmo_sdk.base import COMMON_ERRORS, SessionAdapter, build_session


class Kind(str, Enum):
    """Enum sent as a query param."""

    WEAPON = "weapon"


class Dummy(BaseModel):
    """Minimal schema."""

    ok: bool


def test_client_requires_api_url(monkeypatch):
    monkeypatch.delenv("API_URL", raising=False)
    monkeypatch.setattr("artifactsmmo_sdk.client.load_dotenv", lambda: None)
    with pytest.raises(ValueError, match="API URL"):
        ArtifactsClient(token="t")


def test_client_requires_token(monkeypatch):
    monkeypatch.delenv("TOKEN", raising=False)
    monkeypatch.setattr("artifactsmmo_sdk.client.load_dotenv", lambda: None)
    with pytest.raises(ValueError, match="Token"):
        ArtifactsClient(api_url="http://x")


def test_explicit_args_win_over_env(monkeypatch):
    monkeypatch.setenv("API_URL", "http://env")
    monkeypatch.setenv("TOKEN", "env-token")
    client = ArtifactsClient(token="arg-token", api_url="http://arg")
    assert client.api_url == "http://arg"
    assert client.session.headers["Authorization"] == "Bearer arg-token"


def test_session_has_default_timeout_and_retry():
    session = build_session("t")
    adapter = session.get_adapter("https://x")
    assert isinstance(adapter, SessionAdapter)
    assert adapter.timeout == 30
    assert 429 in adapter.max_retries.status_forcelist


def test_success(client, respond):
    respond(200, {"ok": True})
    message, data = client.items._request("GET", "/x", Dummy, "done")
    assert (message, data) == ("done", Dummy(ok=True))


@pytest.mark.parametrize(("status", "message"), COMMON_ERRORS.items())
def test_common_errors(client, status, message, respond):
    respond(status)
    assert client.items._request("GET", "/x", Dummy, "done") == (message, None)


def test_endpoint_error_overrides_common(client, respond):
    respond(499)
    result = client.items._request("GET", "/x", Dummy, "done", {499: "custom"})
    assert result == ("custom", None)


def test_unknown_error(client, respond):
    respond(500)
    message, data = client.items._request("GET", "/x", Dummy, "done")
    assert message.startswith("Unknown error") and data is None


def test_params_drop_none_and_unwrap_enums(client, respond):
    respond(200, {"ok": True})
    client.items._request(
        "GET", "/x", Dummy, "done", params={"a": None, "type": Kind.WEAPON}
    )
    assert client.session.request.call_args.kwargs["params"] == {"type": "weapon"}


def test_json_drops_none_values(client, respond):
    respond(200, {"ok": True})
    client.items._request("POST", "/x", Dummy, "done", json={"a": 1, "b": None})
    assert client.session.request.call_args.kwargs["json"] == {"a": 1}


def test_json_list_is_sent_as_is(client, respond):
    respond(200, {"ok": True})
    client.items._request("POST", "/x", Dummy, "done", json=[{"a": 1}])
    assert client.session.request.call_args.kwargs["json"] == [{"a": 1}]
