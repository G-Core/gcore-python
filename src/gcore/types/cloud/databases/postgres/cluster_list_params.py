# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ClusterListParams"]


class ClusterListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    limit: int
    """Maximum number of clusters to return"""

    offset: int
    """Number of clusters to skip"""
