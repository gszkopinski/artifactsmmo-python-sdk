"""Test Accounts."""

from os import environ

from dotenv import load_dotenv
from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


load_dotenv()
artifacts_client = ArtifactsClient()


# ACCOUNT
def test_create_account():
    """Tests."""
    result = artifacts_client.accounts.create_account(
        username=environ.get("DEV_USERNAME", "testuser123"),
        password=environ.get("DEV_PASSWORD", "StrongPassword123!"),
        email=environ.get("DEV_EMAIL", "testuser@example.com"),
    )

    assert result
    ic(result)
