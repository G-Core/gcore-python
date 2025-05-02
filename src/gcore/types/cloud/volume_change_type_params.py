# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VolumeChangeTypeParams"]


class VolumeChangeTypeParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    volume_type: Required[Literal["ssd_hiiops", "standard"]]
    """New volume type name"""
