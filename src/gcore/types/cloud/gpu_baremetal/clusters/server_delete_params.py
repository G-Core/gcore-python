# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServerDeleteParams"]


class ServerDeleteParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    cluster_id: Required[str]
    """GPU cluster ID"""

    delete_floatings: bool
    """Set False if you do not want to delete assigned floating IPs"""
