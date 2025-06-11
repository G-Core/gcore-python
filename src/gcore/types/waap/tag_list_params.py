# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TagListParams"]


class TagListParams(TypedDict, total=False):
    limit: int
    """Number of items to return"""

    name: str
    """Filter tags by their name. Supports '\\**' as a wildcard character."""

    offset: int
    """Number of items to skip"""

    ordering: Optional[Literal["name", "readable_name", "reserved", "-name", "-readable_name", "-reserved"]]
    """Determine the field to order results by"""

    readable_name: str
    """Filter tags by their readable name. Supports '\\**' as a wildcard character."""

    reserved: bool
    """Filter to include only reserved tags."""
