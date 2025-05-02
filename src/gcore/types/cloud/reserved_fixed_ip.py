# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .network import Network
from ..._models import BaseModel
from .allowed_address_pairs import AllowedAddressPairs

__all__ = ["ReservedFixedIP", "Attachment", "Reservation"]


class Attachment(BaseModel):
    resource_id: Optional[str] = None
    """Resource ID"""

    resource_type: Optional[str] = None
    """Resource type"""


class Reservation(BaseModel):
    resource_id: Optional[str] = None
    """ID of the instance or load balancer the IP is attached to"""

    resource_type: Optional[str] = None
    """Resource type of the resource the IP is attached to"""

    status: Optional[str] = None
    """IP reservation status"""


class ReservedFixedIP(BaseModel):
    allowed_address_pairs: List[AllowedAddressPairs]
    """Group of subnet masks and/or IP addresses that share the current IP as VIP"""

    attachments: List[Attachment]
    """Reserved fixed IP attachment entities"""

    created_at: datetime
    """Datetime when the reserved fixed IP was created"""

    is_external: bool
    """If reserved fixed IP belongs to a public network"""

    is_vip: bool
    """If reserved fixed IP is a VIP"""

    name: str
    """Reserved fixed IP name"""

    network: Network
    """Network details"""

    network_id: str
    """ID of the network the port is attached to"""

    port_id: str
    """ID of the port underlying the reserved fixed IP"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    reservation: Reservation
    """Reserved fixed IP status with resource type and ID it is attached to"""

    status: str
    """Underlying port status"""

    updated_at: datetime
    """Datetime when the reserved fixed IP was last updated"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    fixed_ip_address: Optional[str] = None
    """IPv4 address of the reserved fixed IP"""

    fixed_ipv6_address: Optional[str] = None
    """IPv6 address of the reserved fixed IP"""

    project_id: Optional[int] = None
    """Project ID"""

    subnet_id: Optional[str] = None
    """ID of the subnet that owns the IP address"""

    subnet_v6_id: Optional[str] = None
    """ID of the subnet that owns the IPv6 address"""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """
