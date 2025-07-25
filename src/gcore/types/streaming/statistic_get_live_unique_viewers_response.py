# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "StatisticGetLiveUniqueViewersResponse",
    "StatisticGetLiveUniqueViewersResponseItem",
    "StatisticGetLiveUniqueViewersResponseItemMetrics",
]


class StatisticGetLiveUniqueViewersResponseItemMetrics(BaseModel):
    streams: List[int]


class StatisticGetLiveUniqueViewersResponseItem(BaseModel):
    client: int

    metrics: StatisticGetLiveUniqueViewersResponseItemMetrics


StatisticGetLiveUniqueViewersResponse: TypeAlias = List[StatisticGetLiveUniqueViewersResponseItem]
