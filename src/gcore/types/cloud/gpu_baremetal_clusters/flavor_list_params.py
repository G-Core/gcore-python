# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    hide_disabled: Optional[bool]
    """Flag for filtering disabled flavors in the region."""

    include_prices: Optional[bool]
    """Set to true if the response should include flavor prices."""
