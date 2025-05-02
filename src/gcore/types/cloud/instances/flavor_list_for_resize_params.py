# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListForResizeParams"]


class FlavorListForResizeParams(TypedDict, total=False):
    project_id: int

    region_id: int

    include_prices: bool
    """Set to true if flavor listing should include flavor prices"""
