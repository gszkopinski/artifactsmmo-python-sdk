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

The SDK covers the whole Artifacts API (v8.2.4): `client.server`, `account`, `accounts`, `characters`, `actions`, `grand_exchange`, `items`, `monsters`, `resources`, `maps`, `events`, `effects`, `npcs`, `tasks`, `achievements`, `badges`, `skins`, `season_rewards`, `leaderboard`, `raids`, `simulation`, `gems_shop`, `game_assistant`.

Every endpoint returns `(message, data)`. `data` is `None` when the call failed
and `message` tells why. Requests have a 30 s timeout and are retried on HTTP 429.

## Development

```bash
uv sync
uv run pytest                 # unit tests, no network
uv run pytest -m live         # read-only calls on the real API, needs TOKEN and API_URL
uv run python scripts/check_openapi.py   # diff the SDK against the OpenAPI spec
uv run ruff check . && uv run mypy src
```
