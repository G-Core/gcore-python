# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetStreamSeriesParams"]


class StatisticGetStreamSeriesParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start of time frame. Datetime in ISO 8601 format."""

    to: Required[str]
    """End of time frame. Datetime in ISO 8601 format."""

    granularity: Literal["1m", "5m", "15m", "1h", "1d"]
    """specifies the time interval for grouping data"""
