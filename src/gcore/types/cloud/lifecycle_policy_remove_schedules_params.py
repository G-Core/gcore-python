# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["LifecyclePolicyRemoveSchedulesParams"]


class LifecyclePolicyRemoveSchedulesParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    schedule_ids: Required[SequenceNotStr[str]]
    """List of schedule IDs."""
