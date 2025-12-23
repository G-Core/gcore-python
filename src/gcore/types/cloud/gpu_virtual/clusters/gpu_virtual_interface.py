# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...tag import Tag
from ...route import Route
from ....._models import BaseModel
from ...ip_version import IPVersion
from ...floating_ip_status import FloatingIPStatus

__all__ = ["GPUVirtualInterface", "FloatingIP", "IPAssignment", "Network", "NetworkSubnet"]


class FloatingIP(BaseModel):
    id: str
    """Floating IP ID"""

    created_at: datetime
    """Datetime when the floating IP was created"""

    fixed_ip_address: Optional[str] = None
    """IP address of the port the floating IP is attached to"""

    floating_ip_address: Optional[str] = None
    """IP Address of the floating IP"""

    port_id: Optional[str] = None
    """Port ID the floating IP is attached to.

    The `fixed_ip_address` is the IP address of the port.
    """

    router_id: Optional[str] = None
    """Router ID"""

    status: Optional[FloatingIPStatus] = None
    """Floating IP status"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    updated_at: datetime
    """Datetime when the floating IP was last updated"""


class IPAssignment(BaseModel):
    ip_address: str
    """The IP address assigned to the port from the specified subnet"""

    subnet_id: str
    """ID of the subnet that allocated the IP"""


class NetworkSubnet(BaseModel):
    id: str
    """Subnet id."""

    available_ips: Optional[int] = None
    """Number of available ips in subnet"""

    cidr: str
    """CIDR"""

    created_at: datetime
    """Datetime when the subnet was created"""

    dns_nameservers: Optional[List[str]] = None
    """List IP addresses of a DNS resolver reachable from the network"""

    enable_dhcp: bool
    """Indicates whether DHCP is enabled for this subnet.

    If true, IP addresses will be assigned automatically
    """

    gateway_ip: Optional[str] = None
    """Default GW IPv4 address, advertised in DHCP routes of this subnet.

    If null, no gateway is advertised by this subnet.
    """

    has_router: bool
    """Deprecated. Always returns `false`."""

    host_routes: Optional[List[Route]] = None
    """List of custom static routes to advertise via DHCP."""

    ip_version: IPVersion
    """IP version used by the subnet (IPv4 or IPv6)"""

    name: str
    """Subnet name"""

    network_id: str
    """Network ID"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    total_ips: Optional[int] = None
    """Total number of ips in subnet"""

    updated_at: datetime
    """Datetime when the subnet was last updated"""


class Network(BaseModel):
    """Body of the network this port is attached to"""

    id: str
    """Network ID"""

    created_at: datetime
    """Datetime when the network was created"""

    external: bool
    """True if the network `router:external` attribute"""

    mtu: int
    """MTU (maximum transmission unit)"""

    name: str
    """Network name"""

    port_security_enabled: bool
    """
    Indicates `port_security_enabled` status of all newly created in the network
    ports.
    """

    segmentation_id: Optional[int] = None
    """Id of network segment"""

    shared: bool
    """True when the network is shared with your project by external owner"""

    subnets: Optional[List[NetworkSubnet]] = None
    """List of subnetworks"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    type: str
    """Network type (vlan, vxlan)"""

    updated_at: datetime
    """Datetime when the network was last updated"""


class GPUVirtualInterface(BaseModel):
    floating_ips: List[FloatingIP]
    """Bodies of floatingips that are NAT-ing ips of this port"""

    ip_assignments: List[IPAssignment]
    """IP addresses assigned to this port"""

    mac_address: Optional[str] = None
    """MAC address of the virtual port"""

    network: Network
    """Body of the network this port is attached to"""

    network_id: str
    """ID of the network the port is attached to"""

    port_id: str
    """ID of virtual ethernet port object"""

    port_security_enabled: bool
    """Port security status"""
