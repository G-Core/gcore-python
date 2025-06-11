# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .tag import Tag
from ..._models import BaseModel
from .ddos_profile import DDOSProfile
from .fixed_address import FixedAddress
from .blackhole_port import BlackholePort
from .floating_address import FloatingAddress
from .instance_isolation import InstanceIsolation
from .fixed_address_short import FixedAddressShort

__all__ = [
    "GPUBaremetalClusterServer",
    "Address",
    "FixedIPAssignment",
    "Flavor",
    "FlavorHardwareDescription",
    "SecurityGroup",
]

Address: TypeAlias = Union[FloatingAddress, FixedAddressShort, FixedAddress]


class FixedIPAssignment(BaseModel):
    external: bool
    """Is network external"""

    ip_address: str
    """Ip address"""

    subnet_id: str
    """Interface subnet id"""


class FlavorHardwareDescription(BaseModel):
    cpu: str
    """Human-readable CPU description"""

    disk: str
    """Human-readable disk description"""

    gpu: str
    """Human-readable GPU description"""

    license: str
    """If the flavor is licensed, this field contains the license type"""

    network: str
    """Human-readable NIC description"""

    ram: str
    """Human-readable RAM description"""


class Flavor(BaseModel):
    architecture: str
    """CPU architecture"""

    flavor_id: str
    """Flavor ID is the same as name"""

    flavor_name: str
    """Flavor name"""

    hardware_description: FlavorHardwareDescription
    """Additional hardware description"""

    os_type: str
    """Operating system"""

    ram: int
    """RAM size in MiB"""

    resource_class: str
    """Flavor resource class for mapping to hardware capacity"""

    vcpus: int
    """Virtual CPU count. For bare metal flavors, it's a physical CPU count"""


class SecurityGroup(BaseModel):
    name: str
    """Name."""


class GPUBaremetalClusterServer(BaseModel):
    id: str
    """GPU server ID"""

    addresses: Dict[str, List[Address]]
    """Map of `network_name` to list of addresses in that network"""

    blackhole_ports: List[BlackholePort]
    """IP addresses of the instances that are blackholed by DDoS mitigation system"""

    created_at: datetime
    """Datetime when GPU server was created"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    ddos_profile: Optional[DDOSProfile] = None
    """Advanced DDoS protection profile.

    It is always `null` if query parameter `with_ddos=true` is not set.
    """

    fixed_ip_assignments: Optional[List[FixedIPAssignment]] = None
    """Fixed IP assigned to instance"""

    flavor: Flavor
    """Flavor"""

    instance_description: Optional[str] = None
    """Instance description"""

    instance_isolation: Optional[InstanceIsolation] = None
    """Instance isolation information"""

    name: str
    """GPU server name"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    security_groups: List[SecurityGroup]
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
