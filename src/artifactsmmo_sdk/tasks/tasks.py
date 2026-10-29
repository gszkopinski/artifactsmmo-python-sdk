"""Tasks."""

from typing import Annotated

from pydantic import Field

from ..base import BaseModule
from ..models.common import (
    TaskType,
)
from ..models.tasks import (
    Skill,
    StaticDataPage_TaskFullSchema_,
    TaskFullResponseSchema,
)


class Tasks(BaseModule):
    """Tasks."""

    def get_all_tasks(
        self,
        min_level: Annotated[
            int | None, Field(description="Minimum level.", ge=0)
        ] = None,
        max_level: Annotated[
            int | None, Field(description="Maximum level.", ge=0)
        ] = None,
        skill: Annotated[Skill | None, Field(description="Skill of tasks.")] = None,
        type: Annotated[TaskType | None, Field(description="Type of tasks.")] = None,
        page: Annotated[int, Field(description="Page number", ge=1)] = 1,
        size: Annotated[int, Field(description="Page size", ge=1, le=10000)] = 50,
    ) -> tuple[str, StaticDataPage_TaskFullSchema_ | None]:
        """Fetch the list of all tasks."""
        return self._request(
            "GET",
            "/tasks/list",
            StaticDataPage_TaskFullSchema_,
            "Successfully fetched tasks.",
            params={
                "min_level": min_level,
                "max_level": max_level,
                "skill": skill,
                "type": type,
                "page": page,
                "size": size,
            },
        )

    def get_task(
        self,
        code: Annotated[
            str, Field(description="The code of the task.", pattern="^[a-zA-Z0-9_-]+$")
        ],
    ) -> tuple[str, TaskFullResponseSchema | None]:
        """Retrieve the details of a task."""
        return self._request(
            "GET",
            f"/tasks/list/{code}",
            TaskFullResponseSchema,
            "Successfully fetched task.",
            {
                404: "task not found.",
            },
        )
