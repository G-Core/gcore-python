# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["StreamSeries", "StreamSeryItem", "StreamSeryItemMetrics"]


class StreamSeryItemMetrics(BaseModel):
    streams: List[int]


class StreamSeryItem(BaseModel):
    client: int

    metrics: StreamSeryItemMetrics


StreamSeries: TypeAlias = List[StreamSeryItem]
