# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ScanResultListParams"]


class ScanResultListParams(TypedDict, total=False):
    limit: int
    """Number of items to return"""

    message: Optional[str]
    """Filter by the message of the scan. Supports '\\**' as a wildcard character"""

    offset: int
    """Number of items to skip"""

    ordering: Literal[
        "id",
        "type",
        "start_time",
        "end_time",
        "status",
        "message",
        "-id",
        "-type",
        "-start_time",
        "-end_time",
        "-status",
        "-message",
    ]
    """Sort the response by given field."""

    status: Optional[Literal["SUCCESS", "FAILURE", "IN_PROGRESS"]]
    """The different statuses a task result can have"""

    type: Optional[Literal["TRAFFIC_SCAN", "API_DESCRIPTION_FILE_SCAN"]]
    """The different types of scans that can be performed"""
