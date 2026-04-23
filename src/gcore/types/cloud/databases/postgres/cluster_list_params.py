# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ClusterListParams"]


class ClusterListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    limit: int
    """Maximum number of clusters to return"""

    name: str
    """Filter clusters by name"""

    offset: int
    """Number of clusters to skip"""
