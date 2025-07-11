# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetDurationSeriesParams"]


class StatisticGetDurationSeriesParams(TypedDict, total=False):
    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Reporting period start time, RFC3339 format"""

    step: Required[int]
    """Reporting granularity, in seconds"""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Reporting period end time (not included into reporting period), RFC3339 format"""

    id: int
    """App ID"""

    network: str
    """Network name"""
