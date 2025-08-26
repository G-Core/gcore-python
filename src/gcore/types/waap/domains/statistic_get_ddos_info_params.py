# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatisticGetDDOSInfoParams"]


class StatisticGetDDOSInfoParams(TypedDict, total=False):
    group_by: Required[Literal["URL", "User-Agent", "IP"]]
    """The identity of the requests to group by"""

    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

    end: Optional[str]
    """Filter data items up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""
