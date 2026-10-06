# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["PolicyOverrideListParams"]


class PolicyOverrideListParams(TypedDict, total=False):
    enabled: Optional[bool]
    """Filter by enabled state."""

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    ordering: Optional[
        Literal[
            "id",
            "name",
            "target_type",
            "enabled",
            "stale",
            "created_at",
            "updated_at",
            "-id",
            "-name",
            "-target_type",
            "-enabled",
            "-stale",
            "-created_at",
            "-updated_at",
        ]
    ]
    """Determine the field used to order results."""

    search: Optional[str]
    """Search policy override names and descriptions."""

    target_type: Optional[Literal["detector", "rule"]]
    """Filter by linked target type."""
