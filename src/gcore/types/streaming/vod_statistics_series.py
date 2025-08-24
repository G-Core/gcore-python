# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["VodStatisticsSeries", "VodStatisticsSeriesItem", "VodStatisticsSeriesItemMetrics"]


class VodStatisticsSeriesItemMetrics(BaseModel):
    vod: List[int]


class VodStatisticsSeriesItem(BaseModel):
    client: int

    metrics: VodStatisticsSeriesItemMetrics


VodStatisticsSeries: TypeAlias = List[VodStatisticsSeriesItem]
