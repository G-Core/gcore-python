# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .waap_domain_status import WaapDomainStatus

__all__ = ["WaapSummaryDomain"]


class WaapSummaryDomain(BaseModel):
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
