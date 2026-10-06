# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["WaapTopDomainDetail"]


class WaapTopDomainDetail(BaseModel):
    attack_types: List[str]
    """Distinct rule names seen for this IP+domain, sorted alphabetically."""

    attacks: int
    """Total detected attacks."""

    blocked: int
    """Blocked attacks."""

    date: datetime
    """First-seen timestamp for the IP+domain within retention period."""

    domain: str
    """Domain name."""

    duration: int
    """`last_seen` - `first_seen` in seconds within retention."""

    paths: int
    """Distinct URL paths excluding query strings."""

    requests: int
    """Total requests."""

    sessions: int
    """Distinct sessions."""

    user_agents: int
    """Distinct user agents."""
