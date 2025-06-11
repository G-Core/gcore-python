# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AllowedAddressPairs"]


class AllowedAddressPairs(BaseModel):
    ip_address: str
    """Subnet mask or IP address of the port specified in `allowed_address_pairs`"""

    mac_address: Optional[str] = None
    """MAC address of the port specified in `allowed_address_pairs`"""
