"""GemsShop schemas."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from .common import ActiveEventSchema, MapContentType


class ActiveEventResponseSchema(BaseModel):
    """ActiveEventResponseSchema"""

    data: ActiveEventSchema


class BuySkinResponseDataSchema(BaseModel):
    """BuySkinResponseDataSchema"""

    skins: list[str]
    skin: str
    gems: int


class BuySkinResponseSchema(BaseModel):
    """BuySkinResponseSchema"""

    data: BuySkinResponseDataSchema


class GemShopCustomDesignCatalogItemSchema(BaseModel):
    """GemShopCustomDesignCatalogItemSchema"""

    code: str
    name: str
    description: str
    price: int
    category: Literal["npc", "item", "skin"]
    unique_to_account: bool


class GemShopSkinCatalogItemSchema(BaseModel):
    """GemShopSkinCatalogItemSchema"""

    code: str
    name: str
    description: str
    price: int


class GemShopSpawnEventCatalogItemSchema(BaseModel):
    """GemShopSpawnEventCatalogItemSchema"""

    code: str
    name: str
    content_type: MapContentType
    content_code: str
    duration: int
    price: int


class GemShopSubscriptionCatalogItemSchema(BaseModel):
    """GemShopSubscriptionCatalogItemSchema"""

    code: str
    name: str
    duration_days: int
    price: int


class GemShopCatalogDataSchema(BaseModel):
    """GemShopCatalogDataSchema"""

    skins: list[GemShopSkinCatalogItemSchema]
    spawn_events: list[GemShopSpawnEventCatalogItemSchema]
    subscriptions: list[GemShopSubscriptionCatalogItemSchema]
    custom_designs: list[GemShopCustomDesignCatalogItemSchema]


class GemShopCatalogResponseSchema(BaseModel):
    """GemShopCatalogResponseSchema"""

    data: GemShopCatalogDataSchema


class GemShopSubscriptionResponseDataSchema(BaseModel):
    """GemShopSubscriptionResponseDataSchema"""

    member: bool
    member_expiration: datetime
    gems: int
    cost: int


class GemShopSubscriptionResponseSchema(BaseModel):
    """GemShopSubscriptionResponseSchema"""

    data: GemShopSubscriptionResponseDataSchema
