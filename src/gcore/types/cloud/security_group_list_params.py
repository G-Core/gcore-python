# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["SecurityGroupListParams"]


class SecurityGroupListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    limit: int
    """Limit the number of returned security groups"""

    offset: int
    """Offset value is used to exclude the first set of records from the result"""

    tag_key: SequenceNotStr[str]
    """Filter by tag keys."""

    tag_key_value: str
    """Filter by tag key-value pairs. Must be a valid JSON string."""
