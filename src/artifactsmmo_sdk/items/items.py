"""Items."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.common import (
    CraftSkill,
    ItemType,
)
from ..models.items import (
    StaticDataPage_ItemSchema_,
)


class Items(BaseModule):
    """Items."""

    def get_all_items(
        self,
        name: Annotated[
            str | None,
            Field(
                description="Name of the item.",
                pattern="^[a-zA-Z0-9_-]+(\\s[a-zA-Z0-9_-]+)*\\s?$",
            ),
        ] = None,
        min_level: Annotated[
            int | None, Field(description="Minimum level.", ge=0)
        ] = None,
        max_level: Annotated[
            int | None, Field(description="Maximum level.", ge=0)
        ] = None,
        type: Annotated[ItemType | None, Field(description="Type of items.")] = None,
        craft_skill: Annotated[
            CraftSkill | None, Field(description="Skill to craft items.")
        ] = None,
        craft_material: Annotated[
            str | None,
            Field(
                description="Item code of items used as material for crafting.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_ItemSchema_ | None]:
        """Fetch items details."""
        return self._request(
            "GET",
            "/items",
            StaticDataPage_ItemSchema_,
            "Successfully fetched items.",
            params={
                "name": name,
                "min_level": min_level,
                "max_level": max_level,
                "type": type,
                "craft_skill": craft_skill,
                "craft_material": craft_material,
                "page": page,
                "size": size,
            },
        )
