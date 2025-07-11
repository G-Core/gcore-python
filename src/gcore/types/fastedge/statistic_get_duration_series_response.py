# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .duration_stats import DurationStats

__all__ = ["StatisticGetDurationSeriesResponse"]


class StatisticGetDurationSeriesResponse(BaseModel):
    stats: List[DurationStats]
