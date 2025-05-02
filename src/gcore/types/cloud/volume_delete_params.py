# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VolumeDeleteParams"]


class VolumeDeleteParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    snapshots: str
    """Comma separated list of snapshot IDs to be deleted with the volume."""
