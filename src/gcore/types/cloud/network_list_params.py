# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["NetworkListParams"]


class NetworkListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    limit: int
    """Limit the number of returned limit request entities."""

    offset: int
    """Offset value is used to exclude the first set of records from the result."""

    order_by: str
    """Order networks by fields and directions (name.asc).

    Default is `created_at.asc`.
    """

    tag_key: List[str]
    """Filter by tag keys."""

    tag_key_value: str
    """Filter by tag key-value pairs.

    Must be a valid JSON string. curl -G --data-urlencode "tag_key_value={"key":
    "value"}" --url "http://localhost:1111/v1/networks/1/1"
    """
