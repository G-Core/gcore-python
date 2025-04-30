# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["RoleAssignment"]


class RoleAssignment(BaseModel):
    id: int
    """
    '#/components/schemas/RoleAssignmentSerializer/properties/id'
    "$.components.schemas.RoleAssignmentSerializer.properties.id"
    """

    assigned_by: Optional[int] = None
    """
    '#/components/schemas/RoleAssignmentSerializer/properties/assigned_by/anyOf/0'
    "$.components.schemas.RoleAssignmentSerializer.properties.assigned_by.anyOf[0]"
    """

    client_id: int
    """
    '#/components/schemas/RoleAssignmentSerializer/properties/client_id'
    "$.components.schemas.RoleAssignmentSerializer.properties.client_id"
    """

    created_at: datetime
    """
    '#/components/schemas/RoleAssignmentSerializer/properties/created_at'
    "$.components.schemas.RoleAssignmentSerializer.properties.created_at"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/RoleAssignmentSerializer/properties/project_id/anyOf/0'
    "$.components.schemas.RoleAssignmentSerializer.properties.project_id.anyOf[0]"
    """

    role: str
    """
    '#/components/schemas/RoleAssignmentSerializer/properties/role'
    "$.components.schemas.RoleAssignmentSerializer.properties.role"
    """

    updated_at: Optional[datetime] = None
    """
    '#/components/schemas/RoleAssignmentSerializer/properties/updated_at/anyOf/0'
    "$.components.schemas.RoleAssignmentSerializer.properties.updated_at.anyOf[0]"
    """

    user_id: int
    """
    '#/components/schemas/RoleAssignmentSerializer/properties/user_id'
    "$.components.schemas.RoleAssignmentSerializer.properties.user_id"
    """
