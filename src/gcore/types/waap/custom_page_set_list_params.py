# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["CustomPageSetListParams"]


class CustomPageSetListParams(TypedDict, total=False):
    ids: Iterable[int]
    """Filter page sets based on their IDs"""

    limit: int
    """Number of items to return"""

    name: str
    """Filter page sets based on their name. Supports '\\**' as a wildcard character"""

    offset: int
    """Number of items to skip"""

    ordering: Literal["name", "-name", "id", "-id"]
    """Sort the response by given field."""
