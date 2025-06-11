# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .quota_item import QuotaItem

__all__ = ["ClientInfo", "Service"]


class Service(BaseModel):
    enabled: bool
    """Whether the service is enabled"""


class ClientInfo(BaseModel):
    id: Optional[int] = None
    """The client ID"""

    features: List[str]
    """List of enabled features"""

    quotas: Dict[str, QuotaItem]
    """Quotas for the client"""

    service: Service
    """Information about the WAAP service status"""
