# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    disabled: bool
    """Flag for filtering disabled flavors in the region. Defaults to true"""

    exclude_linux: bool
    """Set to true to exclude flavors dedicated to linux images. Default False"""

    exclude_windows: bool
    """Set to true to exclude flavors dedicated to windows images. Default False"""

    include_prices: bool
    """Set to true if the response should include flavor prices"""
