# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LifecyclePolicyUpdateParams"]


class LifecyclePolicyUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: str
    """Name of the lifecycle policy."""

    status: Literal["active", "paused"]
    """Status of the lifecycle policy."""
