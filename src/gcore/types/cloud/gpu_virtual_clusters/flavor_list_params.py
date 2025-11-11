# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    hide_disabled: bool
    """Set to `true` to remove the disabled flavors from the response."""

    include_prices: bool
    """Set to `true` if the response should include flavor prices."""
