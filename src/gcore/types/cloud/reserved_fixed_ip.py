# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .network import Network
from ..._models import BaseModel
from .allowed_address_pairs import AllowedAddressPairs

__all__ = ["ReservedFixedIP", "Attachment", "Reservation"]


class Attachment(BaseModel):
    resource_id: Optional[str] = None
    """Resource ID. Null when the attachment's resource is unknown."""

    resource_type: Optional[str] = None
    """Resource type. Null when the attachment's resource type is unknown."""


class Reservation(BaseModel):
    """Reserved fixed IP status with resource type and ID it is attached to"""

    resource_id: Optional[str] = None
    """ID of the instance or load balancer the IP is attached to.

    Null when the IP isn't attached.
    """

    resource_type: Optional[str] = None
    """Resource type of the resource the IP is attached to.

    Null when the IP isn't attached.
    """

    status: Optional[str] = None
    """IP reservation status. Null when the IP isn't attached to a resource."""


class ReservedFixedIP(BaseModel):
    allowed_address_pairs: List[AllowedAddressPairs]
    """Group of subnet masks and/or IP addresses that share the current IP as VIP"""

    attachments: List[Attachment]
    """Reserved fixed IP attachment entities"""

    created_at: datetime
    """Datetime when the reserved fixed IP was created"""

    creator_task_id: Optional[str] = None
    """Task that created this entity.

    Null when the reservation wasn't created via a tracked task.
    """

    fixed_ip_address: Optional[str] = None
    """IPv4 address of the reserved fixed IP.

    Null when the reservation has no IPv4 address.
    """

    fixed_ipv6_address: Optional[str] = None
    """IPv6 address of the reserved fixed IP.

    Null when the reservation has no IPv6 address.
    """

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

    project_id: Optional[int] = None
    """Project ID. Null in an internal, project-less context."""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    reservation: Reservation
    """Reserved fixed IP status with resource type and ID it is attached to"""

    status: str
    """Underlying port status"""

    subnet_id: Optional[str] = None
    """ID of the subnet that owns the IP address.

    Null when the reservation has no IPv4 address.
    """

    subnet_v6_id: Optional[str] = None
    """ID of the subnet that owns the IPv6 address.

    Null when the reservation has no IPv6 address.
    """

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    updated_at: datetime
    """Datetime when the reserved fixed IP was last updated"""
