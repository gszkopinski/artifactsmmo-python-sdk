"""Client SDK for the Artifacts MMO Rest API."""

from os import environ

from dotenv import load_dotenv

from .account import Account
from .accounts import Accounts
from .achievements import Achievements
from .actions import Actions
from .badges import Badges
from .base import build_session
from .characters import Characters
from .effects import Effects
from .events import Events
from .grand_exchange import GrandExchange
from .items import Items
from .leaderboard import Leaderboard
from .maps import Maps
from .monsters import Monsters
from .npcs import Npcs
from .resources import Resources
from .season_rewards import SeasonRewards
from .server import Server
from .skins import Skins
from .tasks import Tasks
from .token import Token


class ArtifactsClient:
    """Client SDK for the Artifacts MMO Rest API."""

    def __init__(
        self,
        token: str | None = None,
        api_url: str | None = None,
    ) -> None:
        """Init the Client."""
        load_dotenv()

        self.api_url = api_url or environ.get("API_URL")
        if not self.api_url:
            msg = "API URL not found: pass api_url or set API_URL"
            raise ValueError(msg)

        api_token = token or environ.get("TOKEN")
        if not api_token:
            msg = "Token not found: pass token or set TOKEN"
            raise ValueError(msg)

        self.session = build_session(api_token)

        self.account = Account(api_url=self.api_url, session=self.session)
        self.accounts = Accounts(api_url=self.api_url, session=self.session)
        self.achievements = Achievements(api_url=self.api_url, session=self.session)
        self.actions = Actions(api_url=self.api_url, session=self.session)
        self.badges = Badges(api_url=self.api_url, session=self.session)
        self.characters = Characters(api_url=self.api_url, session=self.session)
        self.effects = Effects(api_url=self.api_url, session=self.session)
        self.events = Events(api_url=self.api_url, session=self.session)
        self.grand_exchange = GrandExchange(api_url=self.api_url, session=self.session)
        self.items = Items(api_url=self.api_url, session=self.session)
        self.leaderboard = Leaderboard(api_url=self.api_url, session=self.session)
        self.maps = Maps(api_url=self.api_url, session=self.session)
        self.monsters = Monsters(api_url=self.api_url, session=self.session)
        self.npcs = Npcs(api_url=self.api_url, session=self.session)
        self.resources = Resources(api_url=self.api_url, session=self.session)
        self.season_rewards = SeasonRewards(api_url=self.api_url, session=self.session)
        self.server = Server(api_url=self.api_url, session=self.session)
        self.skins = Skins(api_url=self.api_url, session=self.session)
        self.tasks = Tasks(api_url=self.api_url, session=self.session)
        self.token = Token(api_url=self.api_url, session=self.session)
