# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["SecurityGroupListParams"]


class SecurityGroupListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    limit: int
    """Limit the number of returned security groups"""

    offset: int
    """Offset value is used to exclude the first set of records from the result"""

    tag_key: List[str]
    """Filter by tag keys."""

    tag_key_value: str
    """Filter by tag key-value pairs. Must be a valid JSON string."""
