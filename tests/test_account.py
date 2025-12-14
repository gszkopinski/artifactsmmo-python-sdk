"""Test Account."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


artifacts_client = ArtifactsClient()


# BANK
def test_get_bank_details():
    """Tests."""
    result = artifacts_client.account.get_bank_details()

    assert result
    ic(result)


def test_get_bank_items():
    """Tests."""
    result = artifacts_client.account.get_bank_items(
        item_code="iron_sword",
        page=1,
        size=10,
    )

    assert result
    ic(result)


# GRAND EXCHANGE
def test_get_ge_sell_orders():
    """Tests."""
    result = artifacts_client.account.get_ge_sell_orders(
        item_code="iron_sword",
        page=1,
        size=10,
    )

    assert result
    ic(result)


def test_get_ge_sell_history():
    """Tests."""
    result = artifacts_client.account.get_ge_sell_history(
        item_code="iron_sword",
        id="order123",
        page=1,
        size=10,
    )

    assert result
    ic(result)


# ACCOUNT
def test_get_account_details():
    """Tests."""
    result = artifacts_client.account.get_account_details()

    assert result
    ic(result)
