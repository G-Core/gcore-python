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

    architecture: Literal["aarch64", "x86_64"]
    """Filter by image architecture."""

    include_prices: bool
    """Show price."""

    limit: int
    """Optional. Limit the number of returned items"""

    name: str
    """Filter by image name (case-insensitive substring match)"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    os_distro: str
    """Filter by OS distribution (case-insensitive). E.g. `ubuntu`, `centos`, `debian`"""

    os_version: str
    """Filter by OS version (case-insensitive). E.g. `22.04`"""

    private: str
    """Any value to show private images"""

    tag_key: SequenceNotStr[str]
    """Optional. Filter by tag keys. ?`tag_key`=key1&`tag_key`=key2"""

    tag_key_value: str
    """Optional. Filter by tag key-value pairs."""

    visibility: Literal["private", "public", "shared"]
    """Image visibility. Globally visible images are public"""
