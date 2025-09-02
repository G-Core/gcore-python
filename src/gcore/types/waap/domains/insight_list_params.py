# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["InsightListParams"]


class InsightListParams(TypedDict, total=False):
    id: Optional[SequenceNotStr[str]]
    """The ID of the insight"""

    description: Optional[str]
    """The description of the insight. Supports '\\**' as a wildcard."""

    insight_type: Optional[SequenceNotStr[str]]
    """The type of the insight"""

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    ordering: Literal[
        "id",
        "-id",
        "insight_type",
        "-insight_type",
        "first_seen",
        "-first_seen",
        "last_seen",
        "-last_seen",
        "last_status_change",
        "-last_status_change",
        "status",
        "-status",
    ]
    """Sort the response by given field."""

    status: Optional[List[Literal["OPEN", "ACKED", "CLOSED"]]]
    """The status of the insight"""
