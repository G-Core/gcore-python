# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["RoleAssignmentUpdateParams"]


class RoleAssignmentUpdateParams(TypedDict, total=False):
    role: Required[str]
    """
    '#/components/schemas/RequestAssignmentSerializer/properties/role'
    "$.components.schemas.RequestAssignmentSerializer.properties.role"
    """

    user_id: Required[int]
    """
    '#/components/schemas/RequestAssignmentSerializer/properties/user_id'
    "$.components.schemas.RequestAssignmentSerializer.properties.user_id"
    """

    client_id: Optional[int]
    """
    '#/components/schemas/RequestAssignmentSerializer/properties/client_id/anyOf/0'
    "$.components.schemas.RequestAssignmentSerializer.properties.client_id.anyOf[0]"
    """

    project_id: Optional[int]
    """
    '#/components/schemas/RequestAssignmentSerializer/properties/project_id/anyOf/0'
    "$.components.schemas.RequestAssignmentSerializer.properties.project_id.anyOf[0]"
    """
