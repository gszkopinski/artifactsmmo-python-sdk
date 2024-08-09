"""Items."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.items import (
    CraftSkillEnum,
    ListItemsResponseSchema,
    SingleItemResponseSchema,
    TypeItemEnum,
)


class Items:
    """Items."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def get_item(
        self,
        code: Annotated[str, Field(description="The code of the item.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, SingleItemResponseSchema | None]:
        """Retrieve the details of a item."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/items/{code}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched item.",
                SingleItemResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Item not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_all_items(
        self,
        craft_material: Annotated[str, Field(
            description="Item code of items used as material for crafting.",
            pattern="^[a-zA-Z0-9_-]+$",
        )],
        craft_skill: Annotated[CraftSkillEnum, Field(description="Skill to craft items.")],
        max_level: Annotated[int, Field(description="Monster maximum level.", ge=0)],
        min_level: Annotated[int, Field(description="Monster minimum level.", ge=0)],
        name: Annotated[str, Field(description="Name of the item.", pattern="^[a-zA-Z0-9_-]+$")],
        type_item: Annotated[TypeItemEnum, Field(description="Type of items.", alias="type")],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[int, Field(description="Page size.", ge=1, le=100, default=50)] = 50,
    ) -> Tuple[str, ListItemsResponseSchema | None]:
        """Fetch monsters details."""
        try:
            parameters = f"craft_material={craft_material}"
            parameters += f"&craft_skill={craft_skill}"
            parameters += f"&max_level={max_level}"
            parameters += f"&min_level={min_level}"
            parameters += f"&name={name}"
            parameters += f"&page={page}"
            parameters += f"&size={size}"
            parameters += f"&type={type_item}"

            response = self.session.get(
                url=f"{self.api_url}/monsters?{parameters}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched monsters details.",
                ListItemsResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Monsters not found.", None
                case _:
                    return f"Unknown error: {error}", None
