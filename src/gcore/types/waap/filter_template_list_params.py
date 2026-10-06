# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FilterTemplateListParams"]


class FilterTemplateListParams(TypedDict, total=False):
    limit: int
    """Number of items to return"""

    name: str
    """Filter template names by case-insensitive substring match"""

    offset: int
    """Number of items to skip"""
