# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["WaapDDOSAttack"]


class WaapDDOSAttack(BaseModel):
    end_time: Optional[datetime] = None
    """End time of DDoS attack"""

    requests: Optional[int] = None
    """Total DDoS-blocked requests attributed to the attack over its full duration.

    Computed over the attack's own time window, so it stays consistent regardless of
    the selected reporting range. Null when the count could not be computed.
    """

    start_time: Optional[datetime] = None
    """Start time of DDoS attack"""
