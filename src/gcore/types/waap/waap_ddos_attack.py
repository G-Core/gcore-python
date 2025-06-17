# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["WaapDDOSAttack"]


class WaapDDOSAttack(BaseModel):
    end_time: Optional[datetime] = None
    """End time of DDoS attack"""

    start_time: Optional[datetime] = None
    """Start time of DDoS attack"""
