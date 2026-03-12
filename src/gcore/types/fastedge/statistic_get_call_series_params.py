# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetCallSeriesParams"]


class StatisticGetCallSeriesParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Reporting period start time in RFC3339 format"""

    step: Required[int]
    """Reporting time granularity in seconds.

    Common values are 60 (1 minute), 300 (5 minutes), 3600 (1 hour).
    """

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Reporting period end time in RFC3339 format (exclusive)"""

    id: int
    """Filter statistics by specific application ID"""

    network: str
    """Filter statistics by edge network name"""
