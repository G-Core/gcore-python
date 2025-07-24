# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["VodStatisticsSeries", "VodStatisticsSeryItem", "VodStatisticsSeryItemMetrics"]


class VodStatisticsSeryItemMetrics(BaseModel):
    vod: List[int]


class VodStatisticsSeryItem(BaseModel):
    client: int

    metrics: VodStatisticsSeryItemMetrics


VodStatisticsSeries: TypeAlias = List[VodStatisticsSeryItem]
