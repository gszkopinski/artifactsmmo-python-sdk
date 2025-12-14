"""Test Token."""

from os import environ

from dotenv import load_dotenv
from icecream import ic

from artifactsmmo_sdk import ArtifactsClient


load_dotenv()
artifacts_client = ArtifactsClient()


# TOKEN
def test_generate_token():
    """Tests."""
    result = artifacts_client.token.generate_token(
        username=environ.get("DEV_USERNAME", "testuser123"),
        password=environ.get("DEV_PASSWORD", "StrongPassword123!"),
    )

    assert result
    ic(result)
