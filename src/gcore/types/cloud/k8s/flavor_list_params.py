# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    exclude_gpu: bool
    """Set to true to exclude GPU flavors. Default is false."""

    include_capacity: bool
    """Set to true to include flavor capacity. Default is False."""

    include_prices: bool
    """Set to true to include flavor prices. Default is False."""
