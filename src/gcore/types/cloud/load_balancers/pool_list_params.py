# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PoolListParams"]


class PoolListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    details: bool
    """Show members and Health Monitor details"""

    limit: int
    """Optional. Limit the number of returned items"""

    listener_id: str
    """Listener ID"""

    load_balancer_id: str
    """Load Balancer ID"""

    name: str
    """Filter by name"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """
