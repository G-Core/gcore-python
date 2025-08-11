# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RoleAssignmentUpdateParams"]


class RoleAssignmentUpdateParams(TypedDict, total=False):
    role: Required[
        Literal["ClientAdministrator", "InternalNetworkOnlyUser", "Observer", "ProjectAdministrator", "User"]
    ]
    """User role"""

    user_id: Required[int]
    """User ID"""

    client_id: Optional[int]
    """Client ID. Required if `project_id` is specified"""

    project_id: Optional[int]
    """Project ID"""
