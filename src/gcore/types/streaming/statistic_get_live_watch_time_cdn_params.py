# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetLiveWatchTimeCdnParams"]


class StatisticGetLiveWatchTimeCdnParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start of the time period for counting minutes of watching.

    Format is date time in ISO 8601.
    """

    client_user_id: int
    """Filter by field "`client_user_id`" """

    granularity: Literal["1m", "5m", "15m", "1h", "1d", "1mo"]
    """Data is grouped by the specified time interval"""

    stream_id: int
    """Filter by `stream_id`"""

    to: str
    """End of time frame.

    Datetime in ISO 8601 format. If omitted, then the current time is taken
    """
