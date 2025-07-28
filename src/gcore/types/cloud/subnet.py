# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from .route import Route
from ..._models import BaseModel
from .ip_version import IPVersion

__all__ = ["Subnet"]


class Subnet(BaseModel):
    cidr: str
    """CIDR"""

    created_at: datetime
    """Datetime when the subnet was created"""

    enable_dhcp: bool
    """True if DHCP should be enabled"""

    ip_version: IPVersion
    """IP version"""

    name: str
    """Subnet name"""

    network_id: str
    """Network ID"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    updated_at: datetime
    """Datetime when the subnet was last updated"""

    id: Optional[str] = None
    """Subnet id."""

    available_ips: Optional[int] = None
    """Number of available ips in subnet"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    dns_nameservers: Optional[List[str]] = None
    """List IP addresses of a DNS resolver reachable from the network"""

    gateway_ip: Optional[str] = None
    """Default GW IPv4 address, advertised in DHCP routes of this subnet.

    If null, no gateway is advertised by this subnet.
    """

    has_router: Optional[bool] = None
    """Deprecated. Always returns `false`."""

    host_routes: Optional[List[Route]] = None
    """List of custom static routes to advertise via DHCP."""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    total_ips: Optional[int] = None
    """Total number of ips in subnet"""
