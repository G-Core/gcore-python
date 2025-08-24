# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["MaxStreamSeries", "MaxStreamSeriesItem", "MaxStreamSeriesItemMetrics"]


class MaxStreamSeriesItemMetrics(BaseModel):
    streams: List[int]


class MaxStreamSeriesItem(BaseModel):
    client: int

    metrics: MaxStreamSeriesItemMetrics


MaxStreamSeries: TypeAlias = List[MaxStreamSeriesItem]
