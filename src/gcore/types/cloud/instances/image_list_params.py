# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ImageListParams"]


class ImageListParams(TypedDict, total=False):
    project_id: int

    region_id: int

    include_prices: bool
    """Show price"""

    private: str
    """Any value to show private images"""

    tag_key: List[str]
    """Filter by tag keys."""

    tag_key_value: str
    """Filter by tag key-value pairs. Must be a valid JSON string."""

    visibility: Literal["private", "public", "shared"]
    """Image visibility. Globally visible images are public"""
