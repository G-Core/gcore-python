# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PoolListParams"]


class PoolListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    details: bool
    """
    If true, show member and healthmonitor details of each pool (increases request
    time)
    """

    listener_id: str
    """Load balancer listener ID"""

    loadbalancer_id: str
    """Load balancer ID"""
