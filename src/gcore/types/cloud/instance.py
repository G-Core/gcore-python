# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Instance", "Interface", "InterfaceIPAssignment", "InterfaceIPAssignmentFloatingIP", "ManagedBy"]


class InterfaceIPAssignmentFloatingIP(BaseModel):
    """Floating IP that translates this address.

    `null` when the address has no floating IP. An IPv6 address always has `null`.
    """

    id: str
    """Floating IP ID."""

    ip_address: str
    """Public IP address of the floating IP."""


class InterfaceIPAssignment(BaseModel):
    floating_ip: Optional[InterfaceIPAssignmentFloatingIP] = None
    """Floating IP that translates this address.

    `null` when the address has no floating IP. An IPv6 address always has `null`.
    """

    ip_address: str
    """The IP address assigned to the port from the specified subnet"""

    subnet_id: str
    """ID of the subnet that allocated the IP"""


class Interface(BaseModel):
    ip_assignments: List[InterfaceIPAssignment]
    """Fixed IPs assigned to the port, each with its floating IP."""

    mac_address: str
    """Port MAC address."""

    network_id: str
    """Network the port is attached to."""

    port_id: str
    """ID of the port that connects the server to the network."""


class ManagedBy(BaseModel):
    """Service managing this instance, or null if customer-operated."""

    resource_id: Optional[str] = None
    """ID of the managing resource. Null when it is not known."""

    resource_name: str
    """Name of the managing resource."""

    type: Literal["k8s_cluster"]
    """Type of the managing service."""


class Instance(BaseModel):
    id: str
    """Instance ID."""

    boot_volume_id: Optional[str] = None
    """Boot volume ID, or null for an image-backed instance."""

    created_at: datetime
    """Datetime when the instance was created."""

    data_volume_ids: List[str]
    """Non-boot attached volume IDs."""

    flavor_name: str
    """Flavor name."""

    interfaces: List[Interface]
    """Attached network interfaces."""

    managed_by: Optional[ManagedBy] = None
    """Service managing this instance, or null if customer-operated."""

    name: str
    """Instance name."""

    placement_group_id: Optional[str] = None
    """Placement group this instance belongs to, or null."""

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
    """Datetime when the instance was last updated."""
