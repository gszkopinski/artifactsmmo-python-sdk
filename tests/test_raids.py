"""Unit tests of the raids endpoints (mocked, no network)."""


def test_get_all_raids(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "code": "x",
                    "name": "x",
                    "description": "x",
                    "monster": "x",
                    "schedule": {
                        "weekdays": ["monday"],
                        "start_hour_utc": 1,
                        "start_minute_utc": 1,
                        "duration_hours": 1,
                    },
                    "rewards": {
                        "damage_rewards": [
                            {
                                "damage_per_reward": 1,
                                "max_rewards": 1,
                                "items": [{"code": "x", "quantity": 1}],
                            }
                        ],
                        "leaderboard": [
                            {
                                "min_rank": 1,
                                "max_rank": 1,
                                "items": [{"code": "x", "quantity": 1}],
                            }
                        ],
                    },
                    "status": "upcoming",
                    "next_start_at": "2024-01-01T00:00:00Z",
                    "participant_count": 1,
                    "active_instance": {
                        "starts_at": "2024-01-01T00:00:00Z",
                        "ends_at": "2024-01-01T00:00:00Z",
                        "status": "upcoming",
                        "total_hp": 1,
                        "remaining_hp": 1,
                        "participant_count": 1,
                        "ended_at": "2024-01-01T00:00:00Z",
                        "result": "success",
                        "rewards_distributed_at": "2024-01-01T00:00:00Z",
                    },
                    "latest_instance": {
                        "starts_at": "2024-01-01T00:00:00Z",
                        "ends_at": "2024-01-01T00:00:00Z",
                        "status": "upcoming",
                        "total_hp": 1,
                        "remaining_hp": 1,
                        "participant_count": 1,
                        "ended_at": "2024-01-01T00:00:00Z",
                        "result": "success",
                        "rewards_distributed_at": "2024-01-01T00:00:00Z",
                    },
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.raids.get_all_raids()
    assert (message, data is not None) == ("Successfully fetched raids.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/raids")
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_raid(client, respond):
    respond(
        200,
        {
            "data": {
                "code": "x",
                "name": "x",
                "description": "x",
                "monster": "x",
                "schedule": {
                    "weekdays": ["monday"],
                    "start_hour_utc": 1,
                    "start_minute_utc": 1,
                    "duration_hours": 1,
                },
                "rewards": {
                    "damage_rewards": [
                        {
                            "damage_per_reward": 1,
                            "max_rewards": 1,
                            "items": [{"code": "x", "quantity": 1}],
                        }
                    ],
                    "leaderboard": [
                        {
                            "min_rank": 1,
                            "max_rank": 1,
                            "items": [{"code": "x", "quantity": 1}],
                        }
                    ],
                },
                "status": "upcoming",
                "next_start_at": "2024-01-01T00:00:00Z",
                "participant_count": 1,
                "active_instance": {
                    "starts_at": "2024-01-01T00:00:00Z",
                    "ends_at": "2024-01-01T00:00:00Z",
                    "status": "upcoming",
                    "total_hp": 1,
                    "remaining_hp": 1,
                    "participant_count": 1,
                    "ended_at": "2024-01-01T00:00:00Z",
                    "result": "success",
                    "rewards_distributed_at": "2024-01-01T00:00:00Z",
                },
                "latest_instance": {
                    "starts_at": "2024-01-01T00:00:00Z",
                    "ends_at": "2024-01-01T00:00:00Z",
                    "status": "upcoming",
                    "total_hp": 1,
                    "remaining_hp": 1,
                    "participant_count": 1,
                    "ended_at": "2024-01-01T00:00:00Z",
                    "result": "success",
                    "rewards_distributed_at": "2024-01-01T00:00:00Z",
                },
            }
        },
    )
    message, data = client.raids.get_raid(code="x")
    assert (message, data is not None) == ("Successfully fetched raid.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/raids/x")


def test_get_raid_error(client, respond):
    respond(404)
    assert client.raids.get_raid(code="x") == ("raid not found.", None)


def test_get_raid_leaderboard(client, respond):
    respond(
        200,
        {
            "data": [{"position": 1, "account": "x", "points": 1}],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.raids.get_raid_leaderboard(code="x")
    assert (message, data is not None) == (
        "Successfully fetched raid leaderboard.",
        True,
    )
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/raids/x/leaderboard",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}
