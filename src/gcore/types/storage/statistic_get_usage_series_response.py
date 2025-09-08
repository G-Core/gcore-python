# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .usage_series import UsageSeries

__all__ = ["StatisticGetUsageSeriesResponse"]


class StatisticGetUsageSeriesResponse(BaseModel):
    data: Optional[UsageSeries] = None
