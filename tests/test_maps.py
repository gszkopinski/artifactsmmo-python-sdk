"""Unit tests of the maps endpoints (mocked, no network)."""


def test_get_all_maps(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "map_id": 1,
                    "name": "x",
                    "skin": "x",
                    "x": 1,
                    "y": 1,
                    "layer": "interior",
                    "access": {
                        "type": "standard",
                        "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                    },
                    "interactions": {
                        "content": {"type": "monster", "code": "x"},
                        "transition": {
                            "map_id": 1,
                            "x": 1,
                            "y": 1,
                            "layer": "interior",
                            "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                        },
                    },
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.maps.get_all_maps()
    assert (message, data is not None) == ("Successfully fetched maps.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/maps")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_layer_maps(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "map_id": 1,
                    "name": "x",
                    "skin": "x",
                    "x": 1,
                    "y": 1,
                    "layer": "interior",
                    "access": {
                        "type": "standard",
                        "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                    },
                    "interactions": {
                        "content": {"type": "monster", "code": "x"},
                        "transition": {
                            "map_id": 1,
                            "x": 1,
                            "y": 1,
                            "layer": "interior",
                            "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                        },
                    },
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.maps.get_layer_maps(layer="interior")
    assert (message, data is not None) == ("Successfully fetched maps.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/maps/interior",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_map(client, respond):
    respond(
        200,
        {
            "data": {
                "map_id": 1,
                "name": "x",
                "skin": "x",
                "x": 1,
                "y": 1,
                "layer": "interior",
                "access": {
                    "type": "standard",
                    "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                },
                "interactions": {
                    "content": {"type": "monster", "code": "x"},
                    "transition": {
                        "map_id": 1,
                        "x": 1,
                        "y": 1,
                        "layer": "interior",
                        "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                    },
                },
            }
        },
    )
    message, data = client.maps.get_map(layer="interior", x=1, y=1)
    assert (message, data is not None) == ("Successfully fetched map.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/maps/interior/1/1",
    )


def test_get_map_error(client, respond):
    respond(404)
    assert client.maps.get_map(layer="interior", x=1, y=1) == ("map not found.", None)


def test_get_map_by_id(client, respond):
    respond(
        200,
        {
            "data": {
                "map_id": 1,
                "name": "x",
                "skin": "x",
                "x": 1,
                "y": 1,
                "layer": "interior",
                "access": {
                    "type": "standard",
                    "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                },
                "interactions": {
                    "content": {"type": "monster", "code": "x"},
                    "transition": {
                        "map_id": 1,
                        "x": 1,
                        "y": 1,
                        "layer": "interior",
                        "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                    },
                },
            }
        },
    )
    message, data = client.maps.get_map_by_id(map_id=1)
    assert (message, data is not None) == ("Successfully fetched map.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/maps/id/1")


def test_get_map_by_id_error(client, respond):
    respond(404)
    assert client.maps.get_map_by_id(map_id=1) == ("map not found.", None)
