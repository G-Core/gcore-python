# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: int
    """
    '#/components/schemas/ProjectSerializer/properties/id'
    "$.components.schemas.ProjectSerializer.properties.id"
    """

    client_id: int
    """
    '#/components/schemas/ProjectSerializer/properties/client_id'
    "$.components.schemas.ProjectSerializer.properties.client_id"
    """

    created_at: datetime
    """
    '#/components/schemas/ProjectSerializer/properties/created_at'
    "$.components.schemas.ProjectSerializer.properties.created_at"
    """

    is_default: bool
    """
    '#/components/schemas/ProjectSerializer/properties/is_default'
    "$.components.schemas.ProjectSerializer.properties.is_default"
    """

    name: str
    """
    '#/components/schemas/ProjectSerializer/properties/name'
    "$.components.schemas.ProjectSerializer.properties.name"
    """

    state: str
    """
    '#/components/schemas/ProjectSerializer/properties/state'
    "$.components.schemas.ProjectSerializer.properties.state"
    """

    deleted_at: Optional[datetime] = None
    """
    '#/components/schemas/ProjectSerializer/properties/deleted_at/anyOf/0'
    "$.components.schemas.ProjectSerializer.properties.deleted_at.anyOf[0]"
    """

    description: Optional[str] = None
    """
    '#/components/schemas/ProjectSerializer/properties/description/anyOf/0'
    "$.components.schemas.ProjectSerializer.properties.description.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/ProjectSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.ProjectSerializer.properties.task_id.anyOf[0]"
    """
