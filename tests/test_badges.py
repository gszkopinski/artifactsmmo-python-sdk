"""Unit tests of the badges endpoints (mocked, no network)."""


def test_get_all_badges(client, respond):
    respond(
        200,
        {
            "data": [{"code": "x", "season": 1, "description": "x"}],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.badges.get_all_badges()
    assert (message, data is not None) == ("Successfully fetched badges.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/badges")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
