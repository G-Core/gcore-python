# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["OrganizationListParams"]


class OrganizationListParams(TypedDict, total=False):
    limit: int
    """Number of items to return"""

    name: str
    """Filter organizations by their name. Supports '\\**' as a wildcard character."""

    offset: int
    """Number of items to skip"""

    ordering: Optional[Literal["name", "id", "-name", "-id"]]
    """Determine the field to order results by"""
