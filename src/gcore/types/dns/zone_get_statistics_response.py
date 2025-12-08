# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ZoneGetStatisticsResponse"]


class ZoneGetStatisticsResponse(BaseModel):
    """StatisticsZoneResponse"""

    requests: Optional[object] = None
    """
    Requests amount (values) for particular zone fractionated by time intervals
    (keys).

    Example of response:
    `{ "requests": { "1598608080000": 14716, "1598608140000": 51167, "1598608200000": 53432, "1598611020000": 51050, "1598611080000": 52611, "1598611140000": 46884 } }`
    """

    total: Optional[int] = None
    """Total - sum of all values"""
