# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ListenerListParams"]


class ListenerListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    limit: int
    """Optional. Limit the number of returned items"""

    load_balancer_id: str
    """Load Balancer ID"""

    name: str
    """Filter by name"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    show_stats: bool
    """Show stats"""
