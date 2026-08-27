# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapSummaryDomain", "Stats"]


class Stats(BaseModel):
    """Traffic statistics for a domain."""

    attacks_blocked: Optional[int] = None
    """Total number of blocked attacks for the last 30 days"""

    attacks_detected: Optional[int] = None
    """Total number of detected attacks for the last 30 days"""

    total_requests: Optional[int] = None
    """Total number of requests for the last 30 days"""


class WaapSummaryDomain(BaseModel):
    """Represents a WAAP domain with traffic statistics for v2 endpoint."""

    id: int
    """The domain ID"""

    created_at: datetime
    """The date and time the domain was created in ISO 8601 format"""

    custom_page_set: Optional[int] = None
    """The ID of the custom page set"""

    name: str
    """The domain name"""

    status: Literal["active", "bypass", "monitor", "locked"]
    """The different statuses a domain can have"""

    aliases: Optional[List[str]] = None
    """CNAME aliases pointing at this domain's CDN resource"""

    cdn_resource_id: Optional[int] = None
    """The ID of the CDN resource this domain is bound to"""

    stats: Optional[Stats] = None
    """Traffic statistics for a domain."""
