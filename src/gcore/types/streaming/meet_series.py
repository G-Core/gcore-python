# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["MeetSeries", "MeetSeryItem", "MeetSeryItemMetrics"]


class MeetSeryItemMetrics(BaseModel):
    max_meet_usage: Optional[List[int]] = None

    meet: Optional[List[List[int]]] = None


class MeetSeryItem(BaseModel):
    client: int

    metrics: MeetSeryItemMetrics


MeetSeries: TypeAlias = List[MeetSeryItem]
