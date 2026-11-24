# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "BaremetalServer",
    "Interface",
    "InterfaceIPAssignment",
    "InterfaceTrunk",
    "InterfaceTrunkGlobalBaremetalTrunkParentSerializer",
    "InterfaceTrunkGlobalBaremetalTrunkSubPortSerializer",
    "ManagedBy",
]


class InterfaceIPAssignment(BaseModel):
    ip_address: str
    """The IP address assigned to the port from the specified subnet"""

    subnet_id: str
    """ID of the subnet that allocated the IP"""


class InterfaceTrunkGlobalBaremetalTrunkParentSerializer(BaseModel):
    role: Literal["parent"]
    """Role of this interface within its bond/trunk."""


class InterfaceTrunkGlobalBaremetalTrunkSubPortSerializer(BaseModel):
    parent_port_id: str
    """Parent (bond) port ID."""

    role: Literal["sub_port"]
    """Role of this interface within its bond/trunk."""


InterfaceTrunk: TypeAlias = Annotated[
    Union[
        InterfaceTrunkGlobalBaremetalTrunkParentSerializer, InterfaceTrunkGlobalBaremetalTrunkSubPortSerializer, None
    ],
    PropertyInfo(discriminator="role"),
]


class Interface(BaseModel):
    """Bare-metal interface: the VM interface fields plus trunk/bond metadata.

    `port_group` is the 0-based bond index (`null` for DPU/SmartNIC, which has no trunk).
    `trunk` conveys the role within the bond.
    """

    floating_ip: Optional[str] = None
    """Public floating IP NAT-ing this interface, if any."""

    ip_assignments: List[InterfaceIPAssignment]
    """Fixed IPs assigned to the port."""

    mac_address: str
    """Port MAC address."""

    network_id: str
    """Network the port is attached to."""

    port_group: Optional[int] = None
    """0-based bond index. `null` on DPU/SmartNIC bare metal (no trunk)."""

    port_id: str
    """ID of the port that connects the server to the network."""

    trunk: Optional[InterfaceTrunk] = None
    """Trunk role within the bond. `null` when the port is not part of a trunk."""


class ManagedBy(BaseModel):
    """Service managing this server, or null if customer-operated."""

    resource_id: Optional[str] = None
    """ID of the managing resource. Null when it is not known."""

    resource_name: str
    """Name of the managing resource."""

    type: Literal["k8s_cluster"]
    """Type of the managing service."""


class BaremetalServer(BaseModel):
    id: str
    """Baremetal server ID."""

    created_at: datetime
    """Datetime when the server was created."""

    flavor_name: str
    """Flavor name."""

    image_id: str
    """Image ID the server was provisioned from."""

    interfaces: List[Interface]
    """Attached network interfaces with trunk/bond metadata."""

    managed_by: Optional[ManagedBy] = None
    """Service managing this server, or null if customer-operated."""

    name: str
    """Baremetal server name."""

    region_id: int
    """Region ID."""

    ssh_key_id: Optional[str] = None
    """ID of the SSH key of the default user, or null."""

    status: Literal[
        "active",
        "deleted",
        "deleting",
        "error",
        "provisioning",
        "rebooting",
        "rebuilding",
        "resizing",
        "stopped",
        "unknown",
        "updating",
    ]
    """Canonical lifecycle status."""

    system_tags: Dict[str, str]
    """Read-only key-value tags set by the platform."""

    tags: Dict[str, str]
    """Customer-owned key-value tags."""

    updated_at: datetime
    """Datetime when the server was last updated."""
