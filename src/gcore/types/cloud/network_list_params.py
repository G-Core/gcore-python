# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["NetworkListParams"]


class NetworkListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    limit: int
    """Optional. Limit the number of returned items"""

    name: str
    """Filter networks by name"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    order_by: Literal["created_at.asc", "created_at.desc", "name.asc", "name.desc"]
    """
    Ordering networks list result by `name`, `created_at` fields of the network and
    directions (`created_at.desc`).
    """

    tag_key: List[str]
    """Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2"""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""
