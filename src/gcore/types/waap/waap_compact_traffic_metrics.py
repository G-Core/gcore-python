# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WaapCompactTrafficMetrics"]


class WaapCompactTrafficMetrics(BaseModel):
    """Represents the compact traffic metrics for a domain at a given time window"""

    timestamp: int
    """UNIX timestamp indicating when the traffic data was recorded"""

    allowed: Optional[int] = None
    """Traffic passed due to a permissive security rule"""

    blocked: Optional[int] = None
    """Traffic blocked by a security policy, custom rule, or DDoS protection"""

    monitored: Optional[int] = None
    """
    Traffic that was identified as malicious by security policies (for monitored
    domains)
    """

    passed: Optional[int] = None
    """
    Traffic (number of requests) that was passed to the origin and didn't trigger
    any rules
    """
