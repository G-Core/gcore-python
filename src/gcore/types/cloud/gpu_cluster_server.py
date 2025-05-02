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

__all__ = ["GPUClusterServer", "Address", "FixedIPAssignment", "Flavor", "FlavorHardwareDescription", "SecurityGroup"]

Address: TypeAlias = Union[FloatingAddress, FixedAddressShort, FixedAddress]


class FixedIPAssignment(BaseModel):
    external: bool
    """
    '#/components/schemas/IpAssignmentsSerializer/properties/external'
    "$.components.schemas.IpAssignmentsSerializer.properties.external"
    """

    ip_address: str
    """
    '#/components/schemas/IpAssignmentsSerializer/properties/ip_address'
    "$.components.schemas.IpAssignmentsSerializer.properties.ip_address"
    """

    subnet_id: str
    """
    '#/components/schemas/IpAssignmentsSerializer/properties/subnet_id'
    "$.components.schemas.IpAssignmentsSerializer.properties.subnet_id"
    """


class FlavorHardwareDescription(BaseModel):
    cpu: str
    """
    '#/components/schemas/DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer/properties/cpu'
    "$.components.schemas.DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer.properties.cpu"
    """

    disk: str
    """
    '#/components/schemas/DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer/properties/disk'
    "$.components.schemas.DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer.properties.disk"
    """

    gpu: str
    """
    '#/components/schemas/DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer/properties/gpu'
    "$.components.schemas.DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer.properties.gpu"
    """

    license: str
    """
    '#/components/schemas/DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer/properties/license'
    "$.components.schemas.DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer.properties.license"
    """

    network: str
    """
    '#/components/schemas/DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer/properties/network'
    "$.components.schemas.DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer.properties.network"
    """

    ram: str
    """
    '#/components/schemas/DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer/properties/ram'
    "$.components.schemas.DeprecatedAIClusterServerFlavorHardwareDescriptionSerializer.properties.ram"
    """


class Flavor(BaseModel):
    architecture: str
    """
    '#/components/schemas/DeprecatedGpuClusterFlavorSerializer/properties/architecture'
    "$.components.schemas.DeprecatedGpuClusterFlavorSerializer.properties.architecture"
    """

    flavor_id: str
    """
    '#/components/schemas/DeprecatedGpuClusterFlavorSerializer/properties/flavor_id'
    "$.components.schemas.DeprecatedGpuClusterFlavorSerializer.properties.flavor_id"
    """

    flavor_name: str
    """
    '#/components/schemas/DeprecatedGpuClusterFlavorSerializer/properties/flavor_name'
    "$.components.schemas.DeprecatedGpuClusterFlavorSerializer.properties.flavor_name"
    """

    hardware_description: FlavorHardwareDescription
    """
    '#/components/schemas/DeprecatedGpuClusterFlavorSerializer/properties/hardware_description'
    "$.components.schemas.DeprecatedGpuClusterFlavorSerializer.properties.hardware_description"
    """

    os_type: str
    """
    '#/components/schemas/DeprecatedGpuClusterFlavorSerializer/properties/os_type'
    "$.components.schemas.DeprecatedGpuClusterFlavorSerializer.properties.os_type"
    """

    ram: int
    """
    '#/components/schemas/DeprecatedGpuClusterFlavorSerializer/properties/ram'
    "$.components.schemas.DeprecatedGpuClusterFlavorSerializer.properties.ram"
    """

    resource_class: str
    """
    '#/components/schemas/DeprecatedGpuClusterFlavorSerializer/properties/resource_class'
    "$.components.schemas.DeprecatedGpuClusterFlavorSerializer.properties.resource_class"
    """

    vcpus: int
    """
    '#/components/schemas/DeprecatedGpuClusterFlavorSerializer/properties/vcpus'
    "$.components.schemas.DeprecatedGpuClusterFlavorSerializer.properties.vcpus"
    """


class SecurityGroup(BaseModel):
    name: str
    """
    '#/components/schemas/NameSerializerPydantic/properties/name'
    "$.components.schemas.NameSerializerPydantic.properties.name"
    """


class GPUClusterServer(BaseModel):
    addresses: Dict[str, List[Address]]
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/addresses'
    "$.components.schemas.GPUClusterServerSerializer.properties.addresses"
    """

    blackhole_ports: List[BlackholePort]
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/blackhole_ports'
    "$.components.schemas.GPUClusterServerSerializer.properties.blackhole_ports"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.GPUClusterServerSerializer.properties.creator_task_id.anyOf[0]"
    """

    ddos_profile: Optional[DDOSProfile] = None
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/ddos_profile/anyOf/0'
    "$.components.schemas.GPUClusterServerSerializer.properties.ddos_profile.anyOf[0]"
    """

    fixed_ip_assignments: Optional[List[FixedIPAssignment]] = None
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/fixed_ip_assignments/anyOf/0'
    "$.components.schemas.GPUClusterServerSerializer.properties.fixed_ip_assignments.anyOf[0]"
    """

    flavor: Flavor
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/flavor'
    "$.components.schemas.GPUClusterServerSerializer.properties.flavor"
    """

    instance_created: datetime
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/instance_created'
    "$.components.schemas.GPUClusterServerSerializer.properties.instance_created"
    """

    instance_description: Optional[str] = None
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/instance_description/anyOf/0'
    "$.components.schemas.GPUClusterServerSerializer.properties.instance_description.anyOf[0]"
    """

    instance_id: str
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/instance_id'
    "$.components.schemas.GPUClusterServerSerializer.properties.instance_id"
    """

    instance_isolation: Optional[InstanceIsolation] = None
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/instance_isolation/anyOf/0'
    "$.components.schemas.GPUClusterServerSerializer.properties.instance_isolation.anyOf[0]"
    """

    instance_name: str
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/instance_name'
    "$.components.schemas.GPUClusterServerSerializer.properties.instance_name"
    """

    project_id: int
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/project_id'
    "$.components.schemas.GPUClusterServerSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/region'
    "$.components.schemas.GPUClusterServerSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/region_id'
    "$.components.schemas.GPUClusterServerSerializer.properties.region_id"
    """

    security_groups: List[SecurityGroup]
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/security_groups'
    "$.components.schemas.GPUClusterServerSerializer.properties.security_groups"
    """

    ssh_key_name: Optional[str] = None
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/ssh_key_name/anyOf/0'
    "$.components.schemas.GPUClusterServerSerializer.properties.ssh_key_name.anyOf[0]"
    """

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
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/status'
    "$.components.schemas.GPUClusterServerSerializer.properties.status"
    """

    tags: List[Tag]
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/tags'
    "$.components.schemas.GPUClusterServerSerializer.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.GPUClusterServerSerializer.properties.task_id.anyOf[0]"
    """

    task_state: Optional[str] = None
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/task_state/anyOf/0'
    "$.components.schemas.GPUClusterServerSerializer.properties.task_state.anyOf[0]"
    """

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
    """
    '#/components/schemas/GPUClusterServerSerializer/properties/vm_state'
    "$.components.schemas.GPUClusterServerSerializer.properties.vm_state"
    """
