"""Unit tests of the events endpoints (mocked, no network)."""


def test_get_all_active_events(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "map": {
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
                                "conditions": [
                                    {"code": "x", "operator": "eq", "value": 1}
                                ],
                            },
                        },
                    },
                    "previous_map": {
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
                                "conditions": [
                                    {"code": "x", "operator": "eq", "value": 1}
                                ],
                            },
                        },
                    },
                    "duration": 1,
                    "expiration": "2024-01-01T00:00:00Z",
                    "created_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.events.get_all_active_events()
    assert (message, data is not None) == ("Successfully fetched active events.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/events/active",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_all_events(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "name": "x",
                    "code": "x",
                    "content": {"type": "monster", "code": "x"},
                    "maps": [{"map_id": 1, "x": 1, "y": 1, "layer": "x", "skin": "x"}],
                    "duration": 1,
                    "rate": 1,
                    "cooldown": 1,
                    "cooldown_expiration": "2024-01-01T00:00:00Z",
                    "price": 1,
                    "transition": {
                        "map_id": 1,
                        "x": 1,
                        "y": 1,
                        "layer": "interior",
                        "conditions": [{"code": "x", "operator": "eq", "value": 1}],
                    },
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.events.get_all_events()
    assert (message, data is not None) == ("Successfully fetched events.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/events")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
