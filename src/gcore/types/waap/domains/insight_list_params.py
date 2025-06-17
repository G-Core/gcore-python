# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from ..waap_insight_status import WaapInsightStatus
from ..waap_insight_sort_by import WaapInsightSortBy

__all__ = ["InsightListParams"]


class InsightListParams(TypedDict, total=False):
    id: Optional[List[str]]
    """The ID of the insight"""

    description: Optional[str]
    """The description of the insight. Supports '\\**' as a wildcard."""

    insight_type: Optional[List[str]]
    """The type of the insight"""

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    ordering: WaapInsightSortBy
    """Sort the response by given field."""

    status: Optional[List[WaapInsightStatus]]
    """The status of the insight"""
