# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatisticGetUniqueViewersParams"]


class StatisticGetUniqueViewersParams(TypedDict, total=False):
    date_from: Required[str]
    """Start of time frame. Datetime in ISO 8601 format."""

    date_to: Required[str]
    """End of time frame. Datetime in ISO 8601 format."""

    id: str
    """filter by entity's id"""

    country: str
    """filter by country"""

    event: Literal["init", "start", "watch"]
    """filter by event's name"""

    group: List[Literal["date", "host", "os", "browser", "platform", "ip", "country", "event", "id"]]
    """group=1,2,4 OR group=1&group=2&group=3"""

    host: str
    """filter by host"""

    type: Literal["live", "vod", "playlist"]
    """filter by entity's type"""
