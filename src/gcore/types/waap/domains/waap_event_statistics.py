# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .waap_count_statistics import WaapCountStatistics
from .waap_blocked_statistics import WaapBlockedStatistics

__all__ = ["WaapEventStatistics"]


class WaapEventStatistics(BaseModel):
    """A collection of event metrics over a time span"""

    blocked: WaapBlockedStatistics
    """A collection of total numbers of events with blocked results per criteria"""

    count: WaapCountStatistics
    """A collection of total numbers of events per criteria"""
