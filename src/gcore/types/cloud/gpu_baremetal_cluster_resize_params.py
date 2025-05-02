# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GPUBaremetalClusterResizeParams"]


class GPUBaremetalClusterResizeParams(TypedDict, total=False):
    project_id: int

    region_id: int

    instances_count: Required[int]
    """Resized (total) number of instances"""
