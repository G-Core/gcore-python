# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["StreamSeries", "StreamSeriesItem", "StreamSeriesItemMetrics"]


class StreamSeriesItemMetrics(BaseModel):
    streams: List[int]


class StreamSeriesItem(BaseModel):
    client: int

    metrics: StreamSeriesItemMetrics


StreamSeries: TypeAlias = List[StreamSeriesItem]
