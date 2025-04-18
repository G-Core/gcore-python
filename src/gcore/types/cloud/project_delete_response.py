# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ProjectDeleteResponse"]


class ProjectDeleteResponse(BaseModel):
    tasks: Optional[List[str]] = None
    """
    '#/components/schemas/TaskIdListSchema/properties/tasks'
    "$.components.schemas.TaskIdListSchema.properties.tasks"
    """
