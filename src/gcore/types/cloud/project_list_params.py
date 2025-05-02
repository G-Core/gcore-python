# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    client_id: int
    """Client ID filter for administrators."""

    include_deleted: bool
    """Whether to include deleted projects in the response."""

    limit: int
    """Limit value is used to limit the number of records in the result"""

    name: str
    """Name to filter the results by."""

    offset: int
    """Offset value is used to exclude the first set of records from the result"""

    order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"]
    """Order by field and direction."""
