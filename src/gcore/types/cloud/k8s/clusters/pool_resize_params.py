# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PoolResizeParams"]


class PoolResizeParams(TypedDict, total=False):
    project_id: int

    region_id: int

    cluster_name: Required[str]

    node_count: Required[int]
    """Target node count"""
