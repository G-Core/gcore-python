# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SubnetUpdateParams", "HostRoute"]


class SubnetUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    dns_nameservers: Optional[List[str]]
    """List IP addresses of DNS servers to advertise via DHCP."""

    enable_dhcp: Optional[bool]
    """True if DHCP should be enabled"""

    gateway_ip: Optional[str]
    """Default GW IPv4 address to advertise in DHCP routes in this subnet.

    Omit this field to let the cloud backend allocate it automatically. Set to null
    if no gateway must be advertised by this subnet's DHCP (useful when attaching
    instances to multiple subnets in order to prevent default route conflicts).
    """

    host_routes: Optional[Iterable[HostRoute]]
    """List of custom static routes to advertise via DHCP."""

    name: Optional[str]
    """Name"""


class HostRoute(TypedDict, total=False):
    destination: Required[str]
    """CIDR of destination IPv4 subnet."""

    nexthop: Required[str]
    """
    IPv4 address to forward traffic to if it's destination IP matches 'destination'
    CIDR.
    """
