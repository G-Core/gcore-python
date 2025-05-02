# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["RequestListParams"]


class RequestListParams(TypedDict, total=False):
    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    status: Optional[List[Literal["done", "in progress", "rejected"]]]
    """List of limit requests statuses for filtering"""
