# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .storage_usage_series import StorageUsageSeries

__all__ = ["StatisticGetUsageSeriesResponse"]


class StatisticGetUsageSeriesResponse(BaseModel):
    data: Optional[StorageUsageSeries] = None
