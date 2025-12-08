# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WaapDetailedDomain", "Quotas"]


class Quotas(BaseModel):
    allowed: int
    """The maximum allowed number of this resource"""

    current: int
    """The current number of this resource"""


class WaapDetailedDomain(BaseModel):
    """Represents a WAAP domain, serving as a singular unit within the WAAP
    service.

    Each domain functions autonomously, possessing its own set of rules and
    configurations to manage web application firewall settings and
    behaviors.
    """

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

    quotas: Optional[Dict[str, Quotas]] = None
    """Domain level quotas"""
