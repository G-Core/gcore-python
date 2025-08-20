# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RrsetListParams"]


class RrsetListParams(TypedDict, total=False):
    limit: int
    """Max number of records in response"""

    offset: int
    """Amount of records to skip before beginning to write in response."""

    order_by: str
    """Field name to sort by"""

    order_direction: Literal["asc", "desc"]
    """Ascending or descending order"""
