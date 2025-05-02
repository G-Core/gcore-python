# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..subnet import Subnet
from ...._models import BaseModel

__all__ = ["IPWithSubnet"]


class IPWithSubnet(BaseModel):
    ip_address: str
    """IP address"""

    subnet: Subnet
    """Subnet details"""

    subnet_id: str
    """ID of the subnet that allocated the IP"""
