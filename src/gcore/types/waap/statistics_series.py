# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .statistic_item import StatisticItem

__all__ = ["StatisticsSeries"]


class StatisticsSeries(BaseModel):
    total_bytes: Optional[List[StatisticItem]] = None
    """Will be returned if `total_bytes` is requested in the metrics parameter"""

    total_requests: Optional[List[StatisticItem]] = None
    """Will be included if `total_requests` is requested in the metrics parameter"""
