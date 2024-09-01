"""Resources."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.resources import (
    ListResourceResponseSchema,
    ResourceResponseSchema,
    SkillEnum,
)


class Resources:
    """Resources."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def get_resource(
        self,
        code: Annotated[str, Field(description="The code of the monster.", pattern="^[a-zA-Z0-9_-]+$")],
    ) -> Tuple[str, ResourceResponseSchema | None]:
        """Retrieve the details of a resource."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/resources/{code}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched resource.",
                ResourceResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Ressource not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_all_resources(
        self,
        drop: Annotated[str, Field(description="Item code of the drop.", pattern="^[a-zA-Z0-9_-]+$")],
        max_level: Annotated[int, Field(description="Monster maximum level.", ge=0)],
        min_level: Annotated[int, Field(description="Monster minimum level.", ge=0)],
        skill: Annotated[SkillEnum, Field(description="The code of the skill.")],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[int, Field(description="Page size.", ge=1, le=100, default=50)] = 50,
    ) -> Tuple[str, ListResourceResponseSchema | None]:
        """Return resources."""
        try:
            parameters = f"page={page}"
            parameters += f"&size={size}"
            parameters += f"&drop={drop}" if drop else ""
            parameters += f"&max_level={max_level}" if max_level else ""
            parameters += f"&min_level={min_level}" if min_level else ""
            parameters += f"&skill={skill}" if skill else ""

            response = self.session.get(
                url=f"{self.api_url}/resources?{parameters}",
            )

            response.raise_for_status()

            return (
                "",
                ListResourceResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Ressources not found.", None
                case _:
                    return f"Unknown error: {error}", None
