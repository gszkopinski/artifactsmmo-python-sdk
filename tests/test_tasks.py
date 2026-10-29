"""Unit tests of the tasks endpoints (mocked, no network)."""


def test_get_all_tasks(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "code": "x",
                    "level": 1,
                    "type": "monsters",
                    "min_quantity": 1,
                    "max_quantity": 1,
                    "skill": "x",
                    "rewards": {"items": [{"code": "x", "quantity": 1}], "gold": 1},
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.tasks.get_all_tasks()
    assert (message, data is not None) == ("Successfully fetched tasks.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/tasks/list",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_task(client, respond):
    respond(
        200,
        {
            "data": {
                "code": "x",
                "level": 1,
                "type": "monsters",
                "min_quantity": 1,
                "max_quantity": 1,
                "skill": "x",
                "rewards": {"items": [{"code": "x", "quantity": 1}], "gold": 1},
            }
        },
    )
    message, data = client.tasks.get_task(code="x")
    assert (message, data is not None) == ("Successfully fetched task.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/tasks/list/x",
    )


def test_get_task_error(client, respond):
    respond(404)
    assert client.tasks.get_task(code="x") == ("task not found.", None)
