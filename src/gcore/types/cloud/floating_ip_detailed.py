# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .tag import Tag
from ..._models import BaseModel
from .fixed_address import FixedAddress
from .load_balancer import LoadBalancer
from .floating_address import FloatingAddress
from .floating_ip_status import FloatingIPStatus
from .fixed_address_short import FixedAddressShort

__all__ = [
    "FloatingIPDetailed",
    "Instance",
    "InstanceAddress",
    "InstanceFlavor",
    "InstanceSecurityGroup",
    "InstanceVolume",
]

InstanceAddress: TypeAlias = Union[FloatingAddress, FixedAddressShort, FixedAddress]


class InstanceFlavor(BaseModel):
    flavor_id: str
    """Flavor ID is the same as name"""

    flavor_name: str
    """Flavor name"""

    ram: int
    """RAM size in MiB"""

    vcpus: int
    """Virtual CPU count. For bare metal flavors, it's a physical CPU count"""


class InstanceSecurityGroup(BaseModel):
    name: str
    """Name."""


class InstanceVolume(BaseModel):
    id: str
    """Volume ID"""

    delete_on_termination: bool
    """Whether the volume is deleted together with the VM"""


class Instance(BaseModel):
    id: str
    """Instance ID"""

    addresses: Dict[str, List[InstanceAddress]]
    """Map of `network_name` to list of addresses in that network"""

    created_at: datetime
    """Datetime when instance was created"""

    creator_task_id: str
    """Task that created this entity"""

    flavor: InstanceFlavor
    """Flavor"""

    instance_description: Optional[str] = None
    """Instance description"""

    name: str
    """Instance name"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    security_groups: List[InstanceSecurityGroup]
    """Security groups"""

    ssh_key_name: Optional[str] = None
    """SSH key name assigned to instance"""

    status: Literal[
        "ACTIVE",
        "BUILD",
        "DELETED",
        "ERROR",
        "HARD_REBOOT",
        "MIGRATING",
        "PASSWORD",
        "PAUSED",
        "REBOOT",
        "REBUILD",
        "RESCUE",
        "RESIZE",
        "REVERT_RESIZE",
        "SHELVED",
        "SHELVED_OFFLOADED",
        "SHUTOFF",
        "SOFT_DELETED",
        "SUSPENDED",
        "UNKNOWN",
        "VERIFY_RESIZE",
    ]
    """Instance status"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    task_state: Optional[str] = None
    """Task state"""

    vm_state: Literal[
        "active",
        "building",
        "deleted",
        "error",
        "paused",
        "rescued",
        "resized",
        "shelved",
        "shelved_offloaded",
        "soft-deleted",
        "stopped",
        "suspended",
    ]
    """Virtual machine state (active)"""

    volumes: List[InstanceVolume]
    """List of volumes"""


class FloatingIPDetailed(BaseModel):
    id: Optional[str] = None
    """Floating IP ID"""

    created_at: datetime
    """Datetime when the floating IP was created"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    dns_domain: Optional[str] = None
    """This field is deprecated and can be ignored"""

    dns_name: Optional[str] = None
    """This field is deprecated and can be ignored"""

    fixed_ip_address: Optional[str] = None
    """IP address of the port the floating IP is attached to"""

    floating_ip_address: Optional[str] = None
    """IP Address of the floating IP"""

    instance: Optional[Instance] = None
    """Instance the floating IP is attached to"""

    loadbalancer: Optional[LoadBalancer] = None
    """Load balancer the floating IP is attached to"""

    port_id: Optional[str] = None
    """Port ID"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    router_id: Optional[str] = None
    """Router ID"""

    status: Optional[FloatingIPStatus] = None
    """Floating IP status"""

    subnet_id: Optional[str] = None
    """This field is deprecated and can be ignored"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    updated_at: datetime
    """Datetime when the floating IP was last updated"""
