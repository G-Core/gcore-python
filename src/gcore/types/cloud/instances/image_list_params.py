# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ImageListParams"]


class ImageListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    include_prices: bool
    """Show price."""

    private: str
    """Any value to show private images"""

    tag_key: SequenceNotStr[str]
    """Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2"""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""

    visibility: Literal["private", "public", "shared"]
    """Image visibility. Globally visible images are public"""
