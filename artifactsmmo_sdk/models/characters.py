"""Characters Models."""

from enum import Enum
from typing import List

from pydantic import BaseModel


# Character Skin Enum
class CharacterSkinEnum(str, Enum):
    """Character Inventory Model."""

    MEN1 = "men1"
    MEN2 = "men2"
    MEN3 = "men3"
    WOMEN1 = "women1"
    WOMEN2 = "women2"
    WOMEN3 = "women3"


# Character Inventory Model
class CharacterInventorySchema(BaseModel):
    """Character Inventory Model."""

    slot: int
    code: str
    quantity: int


# Character Model
class CharacterSchema(BaseModel):
    """Character Model."""

    name: str
    skin: CharacterSkinEnum
    level: int
    xp: int
    max_xp: int
    total_xp: int
    gold: int
    speed: int
    mining_level: int
    mining_xp: int
    mining_max_xp: int
    woodcutting_level: int
    woodcutting_xp: int
    woodcutting_max_xp: int
    fishing_level: int
    fishing_xp: int
    fishing_max_xp: int
    weaponcrafting_level: int
    weaponcrafting_xp: int
    weaponcrafting_max_xp: int
    gearcrafting_level: int
    gearcrafting_xp: int
    gearcrafting_max_xp: int
    jewelrycrafting_level: int
    jewelrycrafting_xp: int
    jewelrycrafting_max_xp: int
    cooking_level: int
    cooking_xp: int
    cooking_max_xp: int
    hp: int
    haste: int
    critical_strike: int
    stamina: int
    attack_fire: int
    attack_earth: int
    attack_water: int
    attack_air: int
    dmg_fire: int
    dmg_earth: int
    dmg_water: int
    dmg_air: int
    res_fire: int
    res_earth: int
    res_water: int
    res_air: int
    x: int
    y: int
    cooldown: int
    cooldown_expiration: str
    weapon_slot: str
    shield_slot: str
    helmet_slot: str
    body_armor_slot: str
    leg_armor_slot: str
    boots_slot: str
    ring1_slot: str
    ring2_slot: str
    amulet_slot: str
    artifact1_slot: str
    artifact2_slot: str
    artifact3_slot: str
    consumable1_slot: str
    consumable1_slot_quantity: int
    consumable2_slot: str
    consumable2_slot_quantity: int
    task: str
    task_type: str
    task_progress: int
    task_total: int
    inventory_max_items: int
    inventory: List[CharacterInventorySchema]
    # DEPRECATED
    inventory_slot1: str
    inventory_slot1_quantity: int
    inventory_slot2: str
    inventory_slot2_quantity: int
    inventory_slot3: str
    inventory_slot3_quantity: int
    inventory_slot4: str
    inventory_slot4_quantity: int
    inventory_slot5: str
    inventory_slot5_quantity: int
    inventory_slot6: str
    inventory_slot6_quantity: int
    inventory_slot7: str
    inventory_slot7_quantity: int
    inventory_slot8: str
    inventory_slot8_quantity: int
    inventory_slot9: str
    inventory_slot9_quantity: int
    inventory_slot10: str
    inventory_slot10_quantity: int
    inventory_slot11: str
    inventory_slot11_quantity: int
    inventory_slot12: str
    inventory_slot12_quantity: int
    inventory_slot13: str
    inventory_slot13_quantity: int
    inventory_slot14: str
    inventory_slot14_quantity: int
    inventory_slot15: str
    inventory_slot15_quantity: int
    inventory_slot16: str
    inventory_slot16_quantity: int
    inventory_slot17: str
    inventory_slot17_quantity: int
    inventory_slot18: str
    inventory_slot18_quantity: int
    inventory_slot19: str
    inventory_slot19_quantity: int
    inventory_slot20: str
    inventory_slot20_quantity: int


class CharacterResponseSchema(BaseModel):
    """Character Response Model."""

    data: CharacterSchema
