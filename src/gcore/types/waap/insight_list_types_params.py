# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["InsightListTypesParams"]


class InsightListTypesParams(TypedDict, total=False):
    insight_frequency: Optional[int]
    """Filter by the frequency of the insight type"""

    limit: int
    """Number of items to return"""

    name: Optional[str]
    """Filter by the name of the insight type"""

    offset: int
    """Number of items to skip"""

    ordering: Literal["name", "-name", "slug", "-slug", "insight_frequency", "-insight_frequency"]
    """Sort the response by given field."""

    slug: Optional[str]
    """The slug of the insight type"""
