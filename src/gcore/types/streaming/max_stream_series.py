# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["MaxStreamSeries", "MaxStreamSeryItem", "MaxStreamSeryItemMetrics"]


class MaxStreamSeryItemMetrics(BaseModel):
    streams: List[int]


class MaxStreamSeryItem(BaseModel):
    client: int

    metrics: MaxStreamSeryItemMetrics


MaxStreamSeries: TypeAlias = List[MaxStreamSeryItem]
