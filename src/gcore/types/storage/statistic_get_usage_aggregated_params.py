# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["StatisticGetUsageAggregatedParams"]


class StatisticGetUsageAggregatedParams(TypedDict, total=False):
    from_: Annotated[str, PropertyInfo(alias="from")]
    """a From date filter"""

    locations: SequenceNotStr[str]
    """a Locations list of filter"""

    storages: SequenceNotStr[str]
    """a Storages list of filter"""

    to: str
    """a To date filter"""
