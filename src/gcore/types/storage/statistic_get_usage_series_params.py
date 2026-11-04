# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["StatisticGetUsageSeriesParams"]


class StatisticGetUsageSeriesParams(TypedDict, total=False):
    from_: Annotated[str, PropertyInfo(alias="from")]
    """a From date filter"""

    granularity: str
    """
    a Granularity is period of time for grouping data Valid values are: 1h, 12h, 24h
    """

    locations: SequenceNotStr[str]
    """a Locations list of filter"""

    source: int
    """a Source is deprecated parameter"""

    storage_ids: Iterable[int]
    """
    a StorageIDs list of filter, combined with storages. Each ID selects exactly
    that storage, deleted ones included, narrowed by locations. An ID that is not
    one of the client's storages fails the request with 404.
    """

    storages: SequenceNotStr[str]
    """a Storages list of filter"""

    to: str
    """a To date filter"""

    ts_string: bool
    """
    a TsString is configurator of response time format switch response from unix
    time format to RFC3339 (2006-01-02T15:04:05Z07:00)
    """

    accept_language: Annotated[str, PropertyInfo(alias="Accept-Language")]
