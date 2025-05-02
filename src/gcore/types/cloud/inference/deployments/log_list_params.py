# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    order_by: Literal["time.asc", "time.desc"]
    """Order by field"""

    region_id: Optional[int]
    """Region ID"""
