# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "Port",
    "AllowedAddressPair",
    "AttachedTo",
    "AttachedToTrunk",
    "AttachedToTrunkPortAttachmentTrunkParentSerializer",
    "AttachedToTrunkPortAttachmentTrunkSubPortSerializer",
    "Capabilities",
    "IPAssignment",
    "ManagedBy",
]


class AllowedAddressPair(BaseModel):
    ip_address: str
    """Subnet mask or IP address of the allowed address pair"""


class AttachedToTrunkPortAttachmentTrunkParentSerializer(BaseModel):
    role: Literal["parent"]
    """Trunk role. 'parent' means this port is a trunk parent."""


class AttachedToTrunkPortAttachmentTrunkSubPortSerializer(BaseModel):
    parent_port_id: str
    """ID of the trunk parent port this sub-port belongs to."""

    role: Literal["sub_port"]
    """Trunk role. 'sub_port' means this port is a sub-port of a trunk."""


AttachedToTrunk: TypeAlias = Annotated[
    Union[
        AttachedToTrunkPortAttachmentTrunkParentSerializer, AttachedToTrunkPortAttachmentTrunkSubPortSerializer, None
    ],
    PropertyInfo(discriminator="role"),
]


class AttachedTo(BaseModel):
    """
    The compute resource this port is attached to, including trunk role for trunk parents and sub-ports. null when the port is standalone (unattached).
    """

    resource_id: Optional[str] = None
    """ID of the compute resource the port is attached to. null for DHCP attachments."""

    resource_type: Optional[
        Literal[
            "baremetal_server",
            "basic_vm",
            "dhcp",
            "gpu_baremetal_server",
            "gpu_virtual_server",
            "instance",
            "load_balancer",
            "router",
        ]
    ] = None
    """Type of resource the port is attached to.

    null when the compute resource's type is not yet known.
    """

    trunk: Optional[AttachedToTrunk] = None
    """Trunk info: present when port is a trunk parent or `sub_port`. null otherwise."""


class Capabilities(BaseModel):
    """What the driver enforces.

    null when the port is unattached or managed, or when the project sees the port only because it owns the network of the port. null also when this API version does not know the manager type. Such a port is read-only: a change or a delete returns permission-denied.
    """

    allowed_address_pairs: bool
    """Whether the driver enforces allowed address pairs on this port"""

    port_security: bool
    """Whether the driver enforces port security on this port"""

    security_groups: bool
    """Whether the driver enforces security groups on this port"""


class IPAssignment(BaseModel):
    ip_address: str
    """IP address assigned to the port"""

    subnet_id: str
    """ID of the subnet"""


class ManagedBy(BaseModel):
    """Service managing this port.

    null if customer-operated. null also when this API version does not know the manager type. Such a port is read-only: a change or a delete returns permission-denied.
    """

    resource_id: Optional[str] = None
    """ID of the managing resource. Null for system."""

    resource_name: Optional[str] = None
    """Name of the managing resource. Null for system."""

    type: Literal[
        "file_share",
        "gpu_baremetal_cluster",
        "gpu_virtual_cluster",
        "k8s_cluster",
        "load_balancer",
        "network",
        "router",
        "system",
    ]
    """Type of the managing service."""


class Port(BaseModel):
    id: str
    """Port ID"""

    allowed_address_pairs: List[AllowedAddressPair]
    """List of allowed address pairs.

    Sorted by `ip_address` for stable client refreshes.
    """

    attached_to: Optional[AttachedTo] = None
    """
    The compute resource this port is attached to, including trunk role for trunk
    parents and sub-ports. null when the port is standalone (unattached).
    """

    capabilities: Optional[Capabilities] = None
    """What the driver enforces.

    null when the port is unattached or managed, or when the project sees the port
    only because it owns the network of the port. null also when this API version
    does not know the manager type. Such a port is read-only: a change or a delete
    returns permission-denied.
    """

    created_at: datetime
    """Datetime when the port was created."""

    ip_assignments: List[IPAssignment]
    """List of IP addresses assigned to the port."""

    mac_address: str
    """MAC address of the port"""

    managed_by: Optional[ManagedBy] = None
    """Service managing this port.

    null if customer-operated. null also when this API version does not know the
    manager type. Such a port is read-only: a change or a delete returns
    permission-denied.
    """

    network_id: str
    """ID of the network the port belongs to"""

    port_security_enabled: bool
    """
    When true, the driver enforces port security on this port (anti-spoofing checks
    and security-group filtering apply). When false, all traffic is allowed and
    security groups are not applied.
    """

    region_id: int
    """Region ID."""

    security_group_ids: List[str]
    """List of security group IDs applied to the port.

    Sorted lexicographically for stable client refreshes.
    """

    system_tags: Dict[str, str]
    """
    Read-only key-value tags on the port, set by the platform and not modifiable by
    the user
    """

    tags: Dict[str, str]
    """Key-value tags on the port"""

    updated_at: datetime
    """Datetime when the port was last updated."""
