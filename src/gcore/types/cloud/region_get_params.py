# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RegionGetParams"]


class RegionGetParams(TypedDict, total=False):
    region_id: int
    """Region ID"""

    show_volume_types: bool
    """
    If true, null `available_volume_type` is replaced with a list of available
    volume types.
    """
