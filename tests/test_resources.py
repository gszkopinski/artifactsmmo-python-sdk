"""Unit tests of the resources endpoints (mocked, no network)."""


def test_get_all_resources(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "skill": "mining",
                    "level": 1,
                    "drops": [
                        {"code": "x", "rate": 1, "min_quantity": 1, "max_quantity": 1}
                    ],
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.resources.get_all_resources()
    assert (message, data is not None) == ("Successfully fetched resources.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/resources")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_resource(client, respond):
    respond(
        200,
        {
            "data": {
                "name": "x",
                "code": "x",
                "skill": "mining",
                "level": 1,
                "drops": [
                    {"code": "x", "rate": 1, "min_quantity": 1, "max_quantity": 1}
                ],
            }
        },
    )
    message, data = client.resources.get_resource(code="x")
    assert (message, data is not None) == ("Successfully fetched resource.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/resources/x",
    )


def test_get_resource_error(client, respond):
    respond(404)
    assert client.resources.get_resource(code="x") == ("resource not found.", None)
