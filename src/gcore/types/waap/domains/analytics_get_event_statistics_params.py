# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AnalyticsGetEventStatisticsParams"]


class AnalyticsGetEventStatisticsParams(TypedDict, total=False):
    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Filter traffic starting from a specified date in ISO 8601 format"""

    action: Optional[List[Literal["block", "captcha", "handshake", "monitor"]]]
    """A list of action names to filter on."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter traffic up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """

    ip: Optional[List[str]]
    """A list of IPs to filter event statistics."""

    reference_id: Optional[List[str]]
    """A list of reference IDs to filter event statistics."""

    result: Optional[List[Literal["passed", "blocked", "monitored", "allowed"]]]
    """A list of results to filter event statistics."""
