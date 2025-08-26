# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatisticGetTrafficSeriesParams"]


class StatisticGetTrafficSeriesParams(TypedDict, total=False):
    resolution: Required[Literal["daily", "hourly", "minutely"]]
    """Specifies the granularity of the result data."""

    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

    end: Optional[str]
    """Filter data items up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """
