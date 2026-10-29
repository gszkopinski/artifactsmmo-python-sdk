"""Unit tests of the skins endpoints (mocked, no network)."""


def test_get_all_skins(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "code": "x",
                    "name": "x",
                    "description": "x",
                    "default": True,
                    "price": 1,
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.skins.get_all_skins()
    assert (message, data is not None) == ("Successfully fetched skins.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/skins")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
