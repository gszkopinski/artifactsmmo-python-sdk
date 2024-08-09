"""Maps."""

from typing import Annotated, Tuple

import requests

from pydantic import Field

from ..models.maps import ListMapResponseSchema, MapContentTypeSchema, MapResponseSchema


class Maps:
    """Maps."""

    def __init__(
        self,
        api_url: str,
        session: requests.Session,
    ) -> None:
        """Init."""
        self.api_url = api_url
        self.session = session

    def get_map(
        self,
        x: Annotated[int, Field(description="The position X of the map.")],
        y: Annotated[int, Field(description="The position Y of the map.")],
    ) -> Tuple[str, MapResponseSchema | None]:
        """Retrieve the details of a map."""
        try:
            response = self.session.get(
                url=f"{self.api_url}/maps/{x}/{y}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched map.",
                MapResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Map not found.", None
                case _:
                    return f"Unknown error: {error}", None

    def get_all_maps(
        self,
        content_code: Annotated[str, Field(description="Content code on the map.", pattern="^[a-zA-Z0-9_-]+$")],
        content_type: Annotated[MapContentTypeSchema, Field(
            description="Type of content on the map.",
            pattern="^[a-zA-Z0-9_-]+$",
        )],
        page: Annotated[int, Field(description="Page number.", ge=1, default=1)] = 1,
        size: Annotated[int, Field(description="Page size.", ge=1, le=100, default=50)] = 50,
    ) -> Tuple[str, ListMapResponseSchema | None]:
        """Fetch maps details."""
        try:
            parameters = f"content_code={content_code}"
            parameters += f"&content_type={content_type}"
            parameters += f"&page={page}"
            parameters += f"&size={size}"

            response = self.session.get(
                url=f"{self.api_url}/maps?{parameters}",
            )

            response.raise_for_status()

            return (
                "Successfully fetched maps details.",
                ListMapResponseSchema.model_validate(response.json())
            )

        except requests.exceptions.HTTPError as error:
            match error.response.status_code:
                case 404:
                    return "Maps not found.", None
                case _:
                    return f"Unknown error: {error}", None
