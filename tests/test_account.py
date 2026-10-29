"""Unit tests of the account endpoints (mocked, no network)."""


def test_get_bank_details(client, respond):
    respond(
        200,
        {"data": {"slots": 1, "expansions": 1, "next_expansion_cost": 1, "gold": 1}},
    )
    message, data = client.account.get_bank_details()
    assert (message, data is not None) == ("Successfully fetched data.", True)
    assert client.session.request.call_args.args == ("GET", "http://api.test/my/bank")
