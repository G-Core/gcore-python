# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CallStatus", "CountByStatus"]


class CountByStatus(BaseModel):
    count: int
    """Number of app calls"""

    status: int
    """HTTP status"""


class CallStatus(BaseModel):
    count_by_status: List[CountByStatus]
    """Count by status"""

    time: datetime
    """Beginning ot reporting slot"""
