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

    listener_id: str
    """Listener ID"""

    load_balancer_id: str
    """Load Balancer ID"""
