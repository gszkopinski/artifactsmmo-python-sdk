"""Client SDK for the Artifacts MMO Rest API."""

import sys

from os import environ
from typing import Optional

import requests

from dotenv import load_dotenv

from .actions import Actions
from .characters import Characters
from .items import Items
from .maps import Maps
from .monsters import Monsters
from .resources import Resources


load_dotenv()


class ArtifactsClient:
    """Client SDK for the Artifacts MMO Rest API."""

    def __init__(
        self,
        token: Optional[str] = None,
        api_url: Optional[str] = None,
    ) -> None:
        """Init the Client."""
        self.api_url = environ.get("API_URL", api_url)
        if not self.api_url:
            print("API URL not found")
            sys.exit(1)

        self.token = environ.get("TOKEN", token)
        if not self.token:
            print("TOKEN not found")
            sys.exit(1)

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "Accept: application/json",
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
        )

        self.actions = Actions(
            api_url=self.api_url,
            session=self.session,
        )

        self.characters = Characters(
            api_url=self.api_url,
            session=self.session,
        )

        self.items = Items(
            api_url=self.api_url,
            session=self.session,
        )

        self.maps = Maps(
            api_url=self.api_url,
            session=self.session,
        )

        self.monsters = Monsters(
            api_url=self.api_url,
            session=self.session,
        )

        self.resources = Resources(
            api_url=self.api_url,
            session=self.session,
        )
