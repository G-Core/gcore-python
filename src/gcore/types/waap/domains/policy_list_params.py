# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PolicyListParams"]


class PolicyListParams(TypedDict, total=False):
    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    rule_set_id: Optional[int]
    """Filter policies by rule set ID"""
