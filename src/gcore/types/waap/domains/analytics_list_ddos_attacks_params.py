# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AnalyticsListDDOSAttacksParams"]


class AnalyticsListDDOSAttacksParams(TypedDict, total=False):
    end_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter attacks up to a specified end date in ISO 8601 format"""

    limit: int
    """Number of items to return"""

    offset: int
    """Number of items to skip"""

    ordering: Literal["start_time", "-start_time", "end_time", "-end_time"]
    """Sort the response by given field."""

    start_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter attacks starting from a specified date in ISO 8601 format"""
