# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["StorageSeries", "StorageSeriesItem", "StorageSeriesItemMetrics"]


class StorageSeriesItemMetrics(BaseModel):
    max_volume_usage: List[int]

    storage: List[List[int]]


class StorageSeriesItem(BaseModel):
    client: int

    metrics: StorageSeriesItemMetrics


StorageSeries: TypeAlias = List[StorageSeriesItem]
