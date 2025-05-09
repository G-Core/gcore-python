# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel
from .waap_domain_status import WaapDomainStatus

__all__ = ["WaapDetailedDomain", "Quotas"]


class Quotas(BaseModel):
    allowed: int
    """The maximum allowed number of this resource"""

    current: int
    """The current number of this resource"""


class WaapDetailedDomain(BaseModel):
    id: int
    """The domain ID"""

    created_at: datetime
    """The date and time the domain was created in ISO 8601 format"""

    custom_page_set: Optional[int] = None
    """The ID of the custom page set"""

    name: str
    """The domain name"""

    status: WaapDomainStatus
    """The different statuses a domain can have"""

    quotas: Optional[Dict[str, Quotas]] = None
    """Domain level quotas"""
