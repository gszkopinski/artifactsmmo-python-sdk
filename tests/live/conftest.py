"""Live tests: hit the real API, need TOKEN and API_URL (env or .env)."""

import os

import pytest
from dotenv import load_dotenv

load_dotenv()

collect_ignore_glob = (
    [] if os.environ.get("TOKEN") and os.environ.get("API_URL") else ["test_*.py"]
)


def pytest_collection_modifyitems(items):
    """Mark everything under tests/live as live."""
    for item in items:
        if "tests/live/" in str(item.fspath):
            item.add_marker(pytest.mark.live)
