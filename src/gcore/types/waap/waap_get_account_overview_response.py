# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["WaapGetAccountOverviewResponse", "Quotas", "Service"]


class Quotas(BaseModel):
    allowed: int
    """The maximum allowed number of this resource"""

    current: int
    """The current number of this resource"""


class Service(BaseModel):
    enabled: bool
    """Whether the service is enabled"""


class WaapGetAccountOverviewResponse(BaseModel):
    id: Optional[int] = None
    """The client ID"""

    features: List[str]
    """List of enabled features"""

    quotas: Dict[str, Quotas]
    """Quotas for the client"""

    service: Service
    """Information about the WAAP service status"""
