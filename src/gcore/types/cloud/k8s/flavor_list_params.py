# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    exclude_gpu: bool
    """Set to false to include GPU flavors. Default is True."""

    include_prices: bool
    """Set to true to include flavor prices. Default is False."""
