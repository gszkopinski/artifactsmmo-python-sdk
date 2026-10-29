"""Items."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.items import (
    CraftSkillEnum,
    ListItemsResponseSchema,
    SingleItemResponseSchema,
    TypeItemEnum,
)


class Items(BaseModule):
    """Items."""

    def get_item(
        self,
        code: Annotated[
            str, Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$")
        ],
    ) -> tuple[str, SingleItemResponseSchema | None]:
        """Retrieve the details of a item."""
        return self._request(
            "GET",
            f"/items/{code}",
            SingleItemResponseSchema,
            "Successfully fetched item.",
            {
                404: "Item not found.",
            },
        )

    def get_all_items(
        self,
        craft_material: Annotated[
            str,
            Field(
                description="Item code of items used as material for crafting.",
                pattern="^[a-zA-Z0-9_-]+$",
            ),
        ],
        craft_skill: Annotated[
            CraftSkillEnum, Field(description="Skill to craft items.")
        ],
        max_level: Annotated[int, Field(description="Monster maximum level.", ge=0)],
        min_level: Annotated[int, Field(description="Monster minimum level.", ge=0)],
        name: Annotated[
            str, Field(description="Name of the item.", pattern="^[a-zA-Z0-9_-]+$")
        ],
        type_item: Annotated[
            TypeItemEnum, Field(description="Type of items.", alias="type")
        ],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[
            int, Field(description="Page size.", ge=1, le=100, default=50)
        ] = 50,
    ) -> tuple[str, ListItemsResponseSchema | None]:
        """Fetch items details."""
        return self._request(
            "GET",
            "/items",
            ListItemsResponseSchema,
            "Fetch items details.",
            {
                404: "Monsters not found.",
            },
            params={
                "page": page,
                "size": size,
                "type": type_item,
                "craft_material": craft_material or None,
                "craft_skill": craft_skill or None,
                "max_level": max_level or None,
                "min_level": min_level or None,
                "name": name or None,
            },
        )
