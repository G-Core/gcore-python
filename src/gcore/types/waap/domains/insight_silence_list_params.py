# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from ..waap_insight_silence_sort_by import WaapInsightSilenceSortBy

__all__ = ["InsightSilenceListParams"]


class InsightSilenceListParams(TypedDict, total=False):
    id: Optional[List[str]]
    """The ID of the insight silence"""

    author: Optional[str]
    """The author of the insight silence"""

    comment: Optional[str]
    """The comment of the insight silence"""

    insight_type: Optional[List[str]]
    """The type of the insight silence"""

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    ordering: WaapInsightSilenceSortBy
    """Sort the response by given field."""
