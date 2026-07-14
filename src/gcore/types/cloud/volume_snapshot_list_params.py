# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VolumeSnapshotListParams"]


class VolumeSnapshotListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    instance_id: str
    """Optional. Filter snapshots by the instance whose volumes were snapshotted"""

    lifecycle_policy_id: int
    """Optional. Filter by lifecycle policy ID"""

    limit: int
    """Limit of items on a single page"""

    offset: int
    """Offset in results list"""

    schedule_id: str
    """Optional. Filter by schedule ID"""

    volume_id: str
    """Optional. Filter by volume ID"""
