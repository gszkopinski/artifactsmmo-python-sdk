# artifactsmmo-sdk

Python SDK for the [Artifacts MMO](https://artifactsmmo.com) REST API.

## Install

```bash
uv add artifactsmmo-sdk   # or: pip install artifactsmmo-sdk
```

Requires Python 3.12+.

## Usage

Generate a token on the Artifacts website, then either pass it to the client or
set `TOKEN` and `API_URL` (environment or `.env` file).

```python
from artifactsmmo_sdk import ArtifactsClient

client = ArtifactsClient(token="...", api_url="https://api.artifactsmmo.com")

message, result = client.actions.move(name="my_character", x=0, y=1)
if result is None:
    print(message)  # e.g. "Character in cooldown."
```

Every endpoint returns `(message, data)`. `data` is `None` when the call failed
and `message` tells why. Requests have a 30 s timeout and are retried on HTTP 429.

## Development

```bash
uv sync
uv run pytest                 # unit tests, no network
uv run pytest -m live         # hits the real API, needs TOKEN and API_URL
uv run ruff check . && uv run mypy src
```
