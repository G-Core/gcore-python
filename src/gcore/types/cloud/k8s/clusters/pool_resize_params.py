# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PoolResizeParams"]


class PoolResizeParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    cluster_name: Required[str]
    """Cluster name"""

    node_count: Required[int]
    """Target node count"""
