# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..network import Network
from ...._models import BaseModel
from .ip_with_subnet import IPWithSubnet

__all__ = ["ConnectedPort"]


class ConnectedPort(BaseModel):
    instance_id: str
    """ID of the instance that owns the port"""

    instance_name: str
    """Name of the instance that owns the port"""

    ip_assignments: List[IPWithSubnet]
    """IP addresses assigned to this port"""

    network: Network
    """Network details"""

    port_id: str
    """Port ID that shares VIP"""
