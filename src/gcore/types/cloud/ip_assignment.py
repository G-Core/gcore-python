# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["IPAssignment"]


class IPAssignment(BaseModel):
    ip_address: str
    """IP address"""

    subnet_id: str
    """ID of the subnet that allocated the IP"""
