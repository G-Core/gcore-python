# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["WaapTrafficMetrics"]


class WaapTrafficMetrics(BaseModel):
    """Represents the traffic metrics for a domain at a given time window"""

    timestamp: int
    """UNIX timestamp indicating when the traffic data was recorded"""

    ajax: Optional[int] = None
    """Number of AJAX requests made"""

    api: Optional[int] = None
    """Number of API requests made"""

    custom_allowed: Optional[int] = FieldInfo(alias="customAllowed", default=None)
    """Number of requests allowed through custom rules"""

    custom_blocked: Optional[int] = FieldInfo(alias="customBlocked", default=None)
    """Number of requests blocked due to custom rules"""

    ddos_blocked: Optional[int] = FieldInfo(alias="ddosBlocked", default=None)
    """Number of DDoS attack attempts successfully blocked"""

    monitored: Optional[int] = None
    """Number of requests triggering monitoring actions"""

    origin2xx: Optional[int] = None
    """Number of successful HTTP 2xx responses from the origin server"""

    origin3xx: Optional[int] = None
    """Number of HTTP 3xx redirects issued by the origin server"""

    origin_error4xx: Optional[int] = FieldInfo(alias="originError4xx", default=None)
    """Number of HTTP 4xx errors from the origin server"""

    origin_error5xx: Optional[int] = FieldInfo(alias="originError5xx", default=None)
    """Number of HTTP 5xx errors from the origin server"""

    origin_timeout: Optional[int] = FieldInfo(alias="originTimeout", default=None)
    """Number of timeouts experienced at the origin server"""

    passed_to_origin: Optional[int] = FieldInfo(alias="passedToOrigin", default=None)
    """Number of requests served directly by the origin server"""

    policy_allowed: Optional[int] = FieldInfo(alias="policyAllowed", default=None)
    """Number of requests allowed by security policies"""

    policy_blocked: Optional[int] = FieldInfo(alias="policyBlocked", default=None)
    """Number of requests blocked by security policies"""

    response_time: Optional[int] = FieldInfo(alias="responseTime", default=None)
    """Average origin server response time in milliseconds"""

    static: Optional[int] = None
    """Number of static asset requests"""

    total: Optional[int] = None
    """Total number of requests"""

    uncategorized: Optional[int] = None
    """Requests resulting in neither blocks nor sanctions"""
