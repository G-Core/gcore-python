# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["FloatingIPListParams"]


class FloatingIPListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    tag_key: List[str]
    """Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2"""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""
