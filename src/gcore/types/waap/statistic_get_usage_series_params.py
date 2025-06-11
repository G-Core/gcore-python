# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetUsageSeriesParams"]


class StatisticGetUsageSeriesParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Beginning of the requested time period (ISO 8601 format, UTC)"""

    granularity: Required[Literal["1h", "1d"]]
    """Duration of the time blocks into which the data will be divided."""

    metrics: Required[List[Literal["total_bytes", "total_requests"]]]
    """List of metric types to retrieve statistics for."""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End of the requested time period (ISO 8601 format, UTC)"""
