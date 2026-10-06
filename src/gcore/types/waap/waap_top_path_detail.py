# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["WaapTopPathDetail"]


class WaapTopPathDetail(BaseModel):
    date: datetime
    """First seen timestamp for the IP+path within retention period"""

    path: str
    """Path value as stored in logs"""

    attack_types: Optional[List[str]] = None
    """Distinct rule names seen for this IP+path"""

    attacks: Optional[int] = None
    """Total detected attacks (blocked + monitored/suppressed outcomes)"""

    blocked: Optional[int] = None
    """Blocked attacks"""

    duration: Optional[int] = None
    """`last_seen` - `first_seen` in seconds within retention"""

    requests: Optional[int] = None
    """Total requests"""

    sessions: Optional[int] = None
    """Distinct sessions"""

    user_agents: Optional[int] = None
    """Distinct user agents"""
