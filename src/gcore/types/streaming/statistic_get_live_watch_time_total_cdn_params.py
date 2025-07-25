# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetLiveWatchTimeTotalCdnParams"]


class StatisticGetLiveWatchTimeTotalCdnParams(TypedDict, total=False):
    client_user_id: int
    """Filter by field "`client_user_id`" """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Start of the time period for counting minutes of watching.

    Format is date time in ISO 8601. If omitted, the earliest start time for viewing
    is taken
    """

    stream_id: int
    """Filter by `stream_id`"""

    to: str
    """End of time frame.

    Datetime in ISO 8601 format. If missed, then the current time is taken
    """
