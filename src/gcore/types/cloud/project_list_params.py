# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    client_id: Optional[int]
    """Client ID filter for administrators."""

    include_deleted: bool
    """Whether to include deleted entries in the response."""

    name: Optional[str]
    """Name to filter the results by."""

    order_by: Optional[List[Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"]]]
    """Order by field and direction. Supports multiple values."""
