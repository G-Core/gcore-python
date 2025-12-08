# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .waap_statistic_item import WaapStatisticItem

__all__ = ["WaapStatisticsSeries"]


class WaapStatisticsSeries(BaseModel):
    """Response model for the statistics series"""

    total_bytes: Optional[List[WaapStatisticItem]] = None
    """Will be returned if `total_bytes` is requested in the metrics parameter"""

    total_requests: Optional[List[WaapStatisticItem]] = None
    """Will be included if `total_requests` is requested in the metrics parameter"""
