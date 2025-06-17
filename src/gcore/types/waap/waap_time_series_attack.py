# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["WaapTimeSeriesAttack", "Value"]


class Value(BaseModel):
    count: int
    """The number of attacks"""

    timestamp: int
    """The timestamp of the time series item as a POSIX timestamp"""


class WaapTimeSeriesAttack(BaseModel):
    attack_type: str
    """The type of attack"""

    values: List[Value]
    """The time series data"""
