# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["WaapIPDDOSInfoModel", "TimeSeries"]


class TimeSeries(BaseModel):
    count: int
    """The number of attacks"""

    timestamp: int
    """The timestamp of the time series item as a POSIX timestamp"""


class WaapIPDDOSInfoModel(BaseModel):
    botnet_client: bool
    """Indicates if the IP is tagged as a botnet client"""

    time_series: List[TimeSeries]
    """The time series data for the DDoS attacks from the IP address"""
