# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .waap_request_organization import WaapRequestOrganization

__all__ = ["WaapNetworkDetails"]


class WaapNetworkDetails(BaseModel):
    client_ip: str
    """Client IP"""

    country: str
    """Country code"""

    organization: WaapRequestOrganization
    """Organization details"""
