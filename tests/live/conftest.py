"""Live tests: hit the real API, need TOKEN and API_URL (env or .env)."""

import pytest
from dotenv import load_dotenv

load_dotenv()

# TODO: live tests target the pre-v8 SDK; re-enable once they are ported.
collect_ignore_glob = ["test_*.py"]


def pytest_collection_modifyitems(items):
    """Mark everything under tests/live as live."""
    for item in items:
        if "tests/live/" in str(item.fspath):
            item.add_marker(pytest.mark.live)
