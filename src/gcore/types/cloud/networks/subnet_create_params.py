# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr
from ..ip_version import IPVersion

__all__ = ["SubnetCreateParams", "HostRoute"]


class SubnetCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    cidr: Required[str]
    """CIDR"""

    name: Required[str]
    """Subnet name"""

    network_id: Required[str]
    """Network ID"""

    connect_to_network_router: bool
    """True if the network's router should get a gateway in this subnet.

    Must be explicitly 'false' when `gateway_ip` is null.
    """

    dns_nameservers: Optional[SequenceNotStr[str]]
    """List IP addresses of DNS servers to advertise via DHCP."""

    enable_dhcp: bool
    """True if DHCP should be enabled"""

    gateway_ip: Optional[str]
    """Default GW IPv4 address to advertise in DHCP routes in this subnet.

    Omit this field to let the cloud backend allocate it automatically. Set to null
    if no gateway must be advertised by this subnet's DHCP (useful when attaching
    instances to multiple subnets in order to prevent default route conflicts).
    """

    host_routes: Optional[Iterable[HostRoute]]
    """List of custom static routes to advertise via DHCP."""

    ip_version: IPVersion
    """IP version"""

    router_id_to_connect: Optional[str]
    """ID of the router to connect to.

    Requires `connect_to_network_router` set to true. If not specified, attempts to
    find a router created during network creation.
    """

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Both
    tag keys and values have a maximum length of 255 characters. Some tags are
    read-only and cannot be modified by the user. Tags are also integrated with cost
    reports, allowing cost data to be filtered based on tag keys or values.
    """


class HostRoute(TypedDict, total=False):
    destination: Required[str]
    """CIDR of destination IPv4 subnet."""

    nexthop: Required[str]
    """
    IPv4 address to forward traffic to if it's destination IP matches 'destination'
    CIDR.
    """
