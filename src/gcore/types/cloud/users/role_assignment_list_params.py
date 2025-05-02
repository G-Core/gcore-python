# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RoleAssignmentListParams"]


class RoleAssignmentListParams(TypedDict, total=False):
    limit: int
    """Limit the number of returned items.

    Falls back to default of 1000 if not specified. Limited by max limit value of
    1000
    """

    offset: int
    """Offset value is used to exclude the first set of records from the result"""

    project_id: int
    """Project ID"""

    user_id: int
    """User ID for filtering"""
