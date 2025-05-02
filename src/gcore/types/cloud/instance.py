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
    "Instance",
    "Address",
    "FixedIPAssignment",
    "Flavor",
    "FlavorInstanceFlavorSerializer",
    "FlavorInstanceFlavorSerializerHardwareDescription",
    "FlavorBareMetalFlavorSerializer",
    "FlavorBareMetalFlavorSerializerHardwareDescription",
    "FlavorDeprecatedGPUClusterFlavorSerializer",
    "FlavorDeprecatedGPUClusterFlavorSerializerHardwareDescription",
    "SecurityGroup",
    "Volume",
]

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


class FlavorInstanceFlavorSerializerHardwareDescription(BaseModel):
    ram: str
    """
    '#/components/schemas/InstanceFlavorHardwareDescriptionSerializer/properties/ram'
    "$.components.schemas.InstanceFlavorHardwareDescriptionSerializer.properties.ram"
    """

    vcpus: str
    """
    '#/components/schemas/InstanceFlavorHardwareDescriptionSerializer/properties/vcpus'
    "$.components.schemas.InstanceFlavorHardwareDescriptionSerializer.properties.vcpus"
    """


class FlavorInstanceFlavorSerializer(BaseModel):
    architecture: str
    """
    '#/components/schemas/InstanceFlavorSerializer/properties/architecture'
    "$.components.schemas.InstanceFlavorSerializer.properties.architecture"
    """

    flavor_id: str
    """
    '#/components/schemas/InstanceFlavorSerializer/properties/flavor_id'
    "$.components.schemas.InstanceFlavorSerializer.properties.flavor_id"
    """

    flavor_name: str
    """
    '#/components/schemas/InstanceFlavorSerializer/properties/flavor_name'
    "$.components.schemas.InstanceFlavorSerializer.properties.flavor_name"
    """

    hardware_description: FlavorInstanceFlavorSerializerHardwareDescription
    """
    '#/components/schemas/InstanceFlavorSerializer/properties/hardware_description'
    "$.components.schemas.InstanceFlavorSerializer.properties.hardware_description"
    """

    os_type: str
    """
    '#/components/schemas/InstanceFlavorSerializer/properties/os_type'
    "$.components.schemas.InstanceFlavorSerializer.properties.os_type"
    """

    ram: int
    """
    '#/components/schemas/InstanceFlavorSerializer/properties/ram'
    "$.components.schemas.InstanceFlavorSerializer.properties.ram"
    """

    vcpus: int
    """
    '#/components/schemas/InstanceFlavorSerializer/properties/vcpus'
    "$.components.schemas.InstanceFlavorSerializer.properties.vcpus"
    """


class FlavorBareMetalFlavorSerializerHardwareDescription(BaseModel):
    cpu: str
    """
    '#/components/schemas/BareMetalFlavorHardwareDescriptionSerializer/properties/cpu'
    "$.components.schemas.BareMetalFlavorHardwareDescriptionSerializer.properties.cpu"
    """

    disk: str
    """
    '#/components/schemas/BareMetalFlavorHardwareDescriptionSerializer/properties/disk'
    "$.components.schemas.BareMetalFlavorHardwareDescriptionSerializer.properties.disk"
    """

    license: str
    """
    '#/components/schemas/BareMetalFlavorHardwareDescriptionSerializer/properties/license'
    "$.components.schemas.BareMetalFlavorHardwareDescriptionSerializer.properties.license"
    """

    network: str
    """
    '#/components/schemas/BareMetalFlavorHardwareDescriptionSerializer/properties/network'
    "$.components.schemas.BareMetalFlavorHardwareDescriptionSerializer.properties.network"
    """

    ram: str
    """
    '#/components/schemas/BareMetalFlavorHardwareDescriptionSerializer/properties/ram'
    "$.components.schemas.BareMetalFlavorHardwareDescriptionSerializer.properties.ram"
    """


class FlavorBareMetalFlavorSerializer(BaseModel):
    architecture: str
    """
    '#/components/schemas/BareMetalFlavorSerializer/properties/architecture'
    "$.components.schemas.BareMetalFlavorSerializer.properties.architecture"
    """

    flavor_id: str
    """
    '#/components/schemas/BareMetalFlavorSerializer/properties/flavor_id'
    "$.components.schemas.BareMetalFlavorSerializer.properties.flavor_id"
    """

    flavor_name: str
    """
    '#/components/schemas/BareMetalFlavorSerializer/properties/flavor_name'
    "$.components.schemas.BareMetalFlavorSerializer.properties.flavor_name"
    """

    hardware_description: FlavorBareMetalFlavorSerializerHardwareDescription
    """
    '#/components/schemas/BareMetalFlavorSerializer/properties/hardware_description'
    "$.components.schemas.BareMetalFlavorSerializer.properties.hardware_description"
    """

    os_type: str
    """
    '#/components/schemas/BareMetalFlavorSerializer/properties/os_type'
    "$.components.schemas.BareMetalFlavorSerializer.properties.os_type"
    """

    ram: int
    """
    '#/components/schemas/BareMetalFlavorSerializer/properties/ram'
    "$.components.schemas.BareMetalFlavorSerializer.properties.ram"
    """

    resource_class: str
    """
    '#/components/schemas/BareMetalFlavorSerializer/properties/resource_class'
    "$.components.schemas.BareMetalFlavorSerializer.properties.resource_class"
    """

    vcpus: int
    """
    '#/components/schemas/BareMetalFlavorSerializer/properties/vcpus'
    "$.components.schemas.BareMetalFlavorSerializer.properties.vcpus"
    """


class FlavorDeprecatedGPUClusterFlavorSerializerHardwareDescription(BaseModel):
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


class FlavorDeprecatedGPUClusterFlavorSerializer(BaseModel):
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

    hardware_description: FlavorDeprecatedGPUClusterFlavorSerializerHardwareDescription
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


Flavor: TypeAlias = Union[
    FlavorInstanceFlavorSerializer, FlavorBareMetalFlavorSerializer, FlavorDeprecatedGPUClusterFlavorSerializer
]


class SecurityGroup(BaseModel):
    name: str
    """
    '#/components/schemas/NameSerializerPydantic/properties/name'
    "$.components.schemas.NameSerializerPydantic.properties.name"
    """


class Volume(BaseModel):
    id: str
    """
    '#/components/schemas/InstanceVolumeSerializer/properties/id'
    "$.components.schemas.InstanceVolumeSerializer.properties.id"
    """

    delete_on_termination: bool
    """
    '#/components/schemas/InstanceVolumeSerializer/properties/delete_on_termination'
    "$.components.schemas.InstanceVolumeSerializer.properties.delete_on_termination"
    """


class Instance(BaseModel):
    addresses: Dict[str, List[Address]]
    """
    '#/components/schemas/InstanceSerializer/properties/addresses'
    "$.components.schemas.InstanceSerializer.properties.addresses"
    """

    blackhole_ports: List[BlackholePort]
    """
    '#/components/schemas/InstanceSerializer/properties/blackhole_ports'
    "$.components.schemas.InstanceSerializer.properties.blackhole_ports"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/InstanceSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.creator_task_id.anyOf[0]"
    """

    ddos_profile: Optional[DDOSProfile] = None
    """
    '#/components/schemas/InstanceSerializer/properties/ddos_profile/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.ddos_profile.anyOf[0]"
    """

    fixed_ip_assignments: Optional[List[FixedIPAssignment]] = None
    """
    '#/components/schemas/InstanceSerializer/properties/fixed_ip_assignments/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.fixed_ip_assignments.anyOf[0]"
    """

    flavor: Flavor
    """
    '#/components/schemas/InstanceSerializer/properties/flavor'
    "$.components.schemas.InstanceSerializer.properties.flavor"
    """

    instance_created: datetime
    """
    '#/components/schemas/InstanceSerializer/properties/instance_created'
    "$.components.schemas.InstanceSerializer.properties.instance_created"
    """

    instance_description: Optional[str] = None
    """
    '#/components/schemas/InstanceSerializer/properties/instance_description/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.instance_description.anyOf[0]"
    """

    instance_id: str
    """
    '#/components/schemas/InstanceSerializer/properties/instance_id'
    "$.components.schemas.InstanceSerializer.properties.instance_id"
    """

    instance_isolation: Optional[InstanceIsolation] = None
    """
    '#/components/schemas/InstanceSerializer/properties/instance_isolation/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.instance_isolation.anyOf[0]"
    """

    instance_name: str
    """
    '#/components/schemas/InstanceSerializer/properties/instance_name'
    "$.components.schemas.InstanceSerializer.properties.instance_name"
    """

    project_id: int
    """
    '#/components/schemas/InstanceSerializer/properties/project_id'
    "$.components.schemas.InstanceSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/InstanceSerializer/properties/region'
    "$.components.schemas.InstanceSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/InstanceSerializer/properties/region_id'
    "$.components.schemas.InstanceSerializer.properties.region_id"
    """

    security_groups: List[SecurityGroup]
    """
    '#/components/schemas/InstanceSerializer/properties/security_groups'
    "$.components.schemas.InstanceSerializer.properties.security_groups"
    """

    ssh_key_name: Optional[str] = None
    """
    '#/components/schemas/InstanceSerializer/properties/ssh_key_name/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.ssh_key_name.anyOf[0]"
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
    '#/components/schemas/InstanceSerializer/properties/status'
    "$.components.schemas.InstanceSerializer.properties.status"
    """

    tags: List[Tag]
    """
    '#/components/schemas/InstanceSerializer/properties/tags'
    "$.components.schemas.InstanceSerializer.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/InstanceSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.task_id.anyOf[0]"
    """

    task_state: Optional[str] = None
    """
    '#/components/schemas/InstanceSerializer/properties/task_state/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.task_state.anyOf[0]"
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
    '#/components/schemas/InstanceSerializer/properties/vm_state'
    "$.components.schemas.InstanceSerializer.properties.vm_state"
    """

    volumes: List[Volume]
    """
    '#/components/schemas/InstanceSerializer/properties/volumes'
    "$.components.schemas.InstanceSerializer.properties.volumes"
    """
