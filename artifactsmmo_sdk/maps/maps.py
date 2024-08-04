"""Maps."""

import requests

from ..models.maps import ListMapResponseSchema, MapResponseSchema


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
        x: int,
        y: int,
    ) -> MapResponseSchema:
        """Retrieve the details of a map."""
        response = self.session.get(
            url=f"{self.api_url}/maps/{x}/{y}",
        )

        response.raise_for_status()

        return MapResponseSchema.model_validate(response.json())

    def get_all_maps(
        self,
        content_code: str,
        content_type: str,
        page: int = 1,
        size: int = 50,
    ) -> ListMapResponseSchema:
        """Return a map."""
        parameters = f"content_code={content_code}&content_type={content_type}&page={page}&size={size}"
        response = self.session.get(
            url=f"{self.api_url}/maps?{parameters}",
        )

        response.raise_for_status()

        return ListMapResponseSchema.model_validate(response.json())
