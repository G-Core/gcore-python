# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ClusterDeleteParams"]


class ClusterDeleteParams(TypedDict, total=False):
    project_id: int

    region_id: int

    volumes: str
    """Comma separated list of volume IDs to be deleted with the cluster"""
