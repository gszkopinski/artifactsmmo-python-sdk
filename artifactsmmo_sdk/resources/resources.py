"""Resources."""

import requests

from ..models.resources import ResourceResponseSchema, ListResourceResponseSchema


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

    def get_resource(self, x: int, y: int) -> ResourceResponseSchema:
        """Retrieve the details of a resource."""
        response = self.session.get(
            url=f"{self.api_url}/resources/{x}/{y}",
        )

        response.raise_for_status()

        return ResourceResponseSchema.model_validate(response.json())

    def get_all_resources(
        self,
        drop: str,
        max_level: int,
        min_level: int,
        skill:  str,
        page: int = 1,
        size: int = 50,
    ) -> ListResourceResponseSchema:
        """Return resources."""
        parameters = f"drop={drop}"
        parameters += f"&max_level={max_level}"
        parameters += f"&min_level={min_level}"
        parameters += f"&skill={skill}"
        parameters += f"&page={page}"
        parameters += f"&size={size}"

        response = self.session.get(
            url=f"{self.api_url}/resources?{parameters}",
        )

        response.raise_for_status()

        return ListResourceResponseSchema.model_validate(response.json())
