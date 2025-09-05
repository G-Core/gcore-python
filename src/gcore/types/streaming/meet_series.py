# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["MeetSeries", "MeetSeriesItem", "MeetSeriesItemMetrics"]


class MeetSeriesItemMetrics(BaseModel):
    max_meet_usage: Optional[List[int]] = None

    meet: Optional[List[List[int]]] = None


class MeetSeriesItem(BaseModel):
    client: int

    metrics: MeetSeriesItemMetrics


MeetSeries: TypeAlias = List[MeetSeriesItem]
