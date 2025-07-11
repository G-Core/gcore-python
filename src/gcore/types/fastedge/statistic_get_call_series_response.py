# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .call_status import CallStatus

__all__ = ["StatisticGetCallSeriesResponse"]


class StatisticGetCallSeriesResponse(BaseModel):
    stats: List[CallStatus]
