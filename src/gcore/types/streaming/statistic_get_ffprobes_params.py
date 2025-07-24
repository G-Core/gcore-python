# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatisticGetFfprobesParams"]


class StatisticGetFfprobesParams(TypedDict, total=False):
    date_from: Required[str]
    """Start of time frame. Format is ISO 8601."""

    date_to: Required[str]
    """End of time frame. Datetime in ISO 8601 format."""

    stream_id: Required[str]
    """Stream ID"""

    interval: int

    units: Literal["second", "minute", "hour", "day", "week", "month"]
