# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetVodUniqueViewersCdnParams"]


class StatisticGetVodUniqueViewersCdnParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start of time frame. Format is date time in ISO 8601"""

    to: Required[str]
    """End of time frame. Format is date time in ISO 8601"""

    client_user_id: int
    """Filter by user "id" """

    granularity: Literal["1m", "5m", "15m", "1h", "1d"]
    """Specifies the time interval for grouping data"""

    slug: str
    """Filter by video "slug" """
