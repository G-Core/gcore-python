# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnalyticsGetTrafficParams"]


class AnalyticsGetTrafficParams(TypedDict, total=False):
    resolution: Required[Literal["daily", "hourly", "minutely"]]
    """Specifies the granularity of the result data."""

    start: Required[str]
    """Filter data items starting from a specified date in ISO 8601 format"""

    bucket_size: Optional[Literal[60, 300, 600, 900, 1800, 3600, 7200, 10800, 21600, 43200, 86400]]
    """Optional explicit aggregation bucket width in seconds.

    When supplied, `bucket_size` supersedes `resolution` for aggregation
    granularity.
    """

    domains: Iterable[int]
    """List of domain IDs.

    Empty list means all domains belonging to the current account.
    """

    end: Optional[str]
    """Filter data items up to a specified end date in ISO 8601 format.

    If not provided, defaults to the current date and time.
    """
