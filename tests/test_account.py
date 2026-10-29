"""Unit tests of the account endpoints (mocked, no network)."""


def test_get_bank_details(client, respond):
    respond(
        200,
        {"data": {"slots": 1, "expansions": 1, "next_expansion_cost": 1, "gold": 1}},
    )
    message, data = client.account.get_bank_details()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/my/bank")


def test_get_bank_items(client, respond):
    respond(
        200,
        {
            "data": [{"code": "x", "quantity": 1}],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.account.get_bank_items()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/bank/items",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_ge_sell_orders(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "id": "x",
                    "type": "sell",
                    "account": "x",
                    "code": "x",
                    "quantity": 1,
                    "price": 1,
                    "created_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.account.get_ge_sell_orders()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/grandexchange/orders",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_ge_sell_history(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "order_id": "x",
                    "seller": "x",
                    "buyer": "x",
                    "code": "x",
                    "quantity": 1,
                    "price": 1,
                    "sold_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.account.get_ge_sell_history()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/grandexchange/history",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_account_details(client, respond):
    respond(
        200,
        {
            "data": {
                "username": "x",
                "email": "a@b.co",
                "member": True,
                "member_expiration": "2024-01-01T00:00:00Z",
                "status": "standard",
                "badges": ["x"],
                "skins": ["x"],
                "gems": 1,
                "member_token": 1,
                "achievements_points": 1,
                "banned": True,
                "ban_reason": "x",
            }
        },
    )
    message, data = client.account.get_account_details()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/details",
    )


def test_get_pending_items(client, respond):
    respond(
        200,
        {
            "data": [
                {
                    "id": "x",
                    "account": "x",
                    "source": "achievement",
                    "source_id": "x",
                    "description": "x",
                    "gold": 1,
                    "items": [{"code": "x", "quantity": 1}],
                    "created_at": "2024-01-01T00:00:00Z",
                    "claimed_at": "2024-01-01T00:00:00Z",
                }
            ],
            "total": 1,
            "page": 1,
            "size": 1,
            "pages": 1,
        },
    )
    message, data = client.account.get_pending_items()
    assert (message, data is not None) == ("Successfully fetched pending items.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/pending_items",
    )
    assert client.session.request.call_args.kwargs["params"] == {"page": 1, "size": 50}


def test_get_rate_limits(client, respond):
    respond(
        200,
        {
            "data": {
                "account": {
                    "second": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "minute": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "hour": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "day": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                },
                "data": {
                    "second": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "minute": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "hour": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "day": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                },
                "action": {
                    "second": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "minute": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "hour": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "day": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                },
                "simulation": {
                    "second": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "minute": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "hour": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "day": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                },
                "assistant": {
                    "second": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "minute": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "hour": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                    "day": {
                        "limit": 1,
                        "remaining": 1,
                        "reset": "2024-01-01T00:00:00Z",
                    },
                },
            }
        },
    )
    message, data = client.account.get_rate_limits()
    assert (message, data is not None) == ("Successfully fetched rate limits.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/my/rates")


def test_change_password(client, respond):
    respond(200, {"message": "x"})
    message, data = client.account.change_password(
        current_password="x", new_password="x"
    )
    assert (message, data is not None) == ("Password changed successfully.", True)
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/my/change_password",
    )
    assert client.session.request.call_args.kwargs["json"] == {
        "current_password": "x",
        "new_password": "x",
    }


def test_change_password_error(client, respond):
    respond(458)
    assert client.account.change_password(current_password="x", new_password="x") == (
        "Please use a different password.",
        None,
    )


def test_change_email(client, respond):
    respond(200, {"message": "x"})
    message, data = client.account.change_email(
        current_email="a@b.co", new_email="a@b.co"
    )
    assert (message, data is not None) == ("Email changed successfully.", True)
    assert client.session.request.call_args.args == (
        "POST",
        "http://api.test/my/change_email",
    )
    assert client.session.request.call_args.kwargs["json"] == {
        "current_email": "a@b.co",
        "new_email": "a@b.co",
    }


def test_change_email_error(client, respond):
    respond(457)
    assert client.account.change_email(current_email="a@b.co", new_email="a@b.co") == (
        "This email is already in use.",
        None,
    )


def test_get_my_subscription(client, respond):
    respond(
        200,
        {
            "data": {
                "plan": "monthly",
                "purchase_source": "stripe",
                "status": "x",
                "current_period_start": "2024-01-01T00:00:00Z",
                "current_period_end": "2024-01-01T00:00:00Z",
                "created_at": "2024-01-01T00:00:00Z",
                "cancelled_at": "2024-01-01T00:00:00Z",
            }
        },
    )
    message, data = client.account.get_my_subscription()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == (
        "GET",
        "http://api.test/my/subscription",
    )


def test_get_my_subscription_error(client, respond):
    respond(404)
    assert client.account.get_my_subscription() == ("Subscription not found.", None)
