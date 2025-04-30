# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .tag import Tag
from ..._models import BaseModel
from .ddos_profile import DDOSProfile

__all__ = [
    "Instance",
    "Address",
    "AddressInstanceFloatingAddressSerializer",
    "AddressInstanceFixedAddressShortSerializer",
    "AddressInstanceFixedAddressSerializer",
    "BlackholePort",
    "FixedIPAssignment",
    "Flavor",
    "FlavorInstanceFlavorSerializer",
    "FlavorInstanceFlavorSerializerHardwareDescription",
    "FlavorBareMetalFlavorSerializer",
    "FlavorBareMetalFlavorSerializerHardwareDescription",
    "FlavorDeprecatedGPUClusterFlavorSerializer",
    "FlavorDeprecatedGPUClusterFlavorSerializerHardwareDescription",
    "InstanceIsolation",
    "SecurityGroup",
    "Volume",
]


class AddressInstanceFloatingAddressSerializer(BaseModel):
    addr: str
    """
    '#/components/schemas/InstanceFloatingAddressSerializer/properties/addr'
    "$.components.schemas.InstanceFloatingAddressSerializer.properties.addr"
    """

    type: Literal["floating"]
    """
    '#/components/schemas/InstanceFloatingAddressSerializer/properties/type'
    "$.components.schemas.InstanceFloatingAddressSerializer.properties.type"
    """


class AddressInstanceFixedAddressShortSerializer(BaseModel):
    addr: str
    """
    '#/components/schemas/InstanceFixedAddressShortSerializer/properties/addr'
    "$.components.schemas.InstanceFixedAddressShortSerializer.properties.addr"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceFixedAddressShortSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceFixedAddressShortSerializer.properties.interface_name.anyOf[0]"
    """

    type: Literal["fixed"]
    """
    '#/components/schemas/InstanceFixedAddressShortSerializer/properties/type'
    "$.components.schemas.InstanceFixedAddressShortSerializer.properties.type"
    """


class AddressInstanceFixedAddressSerializer(BaseModel):
    addr: str
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/addr'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.addr"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.interface_name.anyOf[0]"
    """

    subnet_id: str
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/subnet_id'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.subnet_id"
    """

    subnet_name: str
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/subnet_name'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.subnet_name"
    """

    type: Literal["fixed"]
    """
    '#/components/schemas/InstanceFixedAddressSerializer/properties/type'
    "$.components.schemas.InstanceFixedAddressSerializer.properties.type"
    """


Address: TypeAlias = Union[
    AddressInstanceFloatingAddressSerializer,
    AddressInstanceFixedAddressShortSerializer,
    AddressInstanceFixedAddressSerializer,
]


class BlackholePort(BaseModel):
    alarm_end: datetime = FieldInfo(alias="AlarmEnd")
    """
    '#/components/schemas/BlackholePortSerializer/properties/AlarmEnd'
    "$.components.schemas.BlackholePortSerializer.properties.AlarmEnd"
    """

    alarm_start: datetime = FieldInfo(alias="AlarmStart")
    """
    '#/components/schemas/BlackholePortSerializer/properties/AlarmStart'
    "$.components.schemas.BlackholePortSerializer.properties.AlarmStart"
    """

    alarm_state: Literal[
        "ACK_REQ",
        "ALARM",
        "ARCHIVED",
        "CLEAR",
        "CLEARING",
        "CLEARING_FAIL",
        "END_GRACE",
        "END_WAIT",
        "MANUAL_CLEAR",
        "MANUAL_CLEARING",
        "MANUAL_CLEARING_FAIL",
        "MANUAL_MITIGATING",
        "MANUAL_STARTING",
        "MANUAL_STARTING_FAIL",
        "MITIGATING",
        "STARTING",
        "STARTING_FAIL",
        "START_WAIT",
        "ack_req",
        "alarm",
        "archived",
        "clear",
        "clearing",
        "clearing_fail",
        "end_grace",
        "end_wait",
        "manual_clear",
        "manual_clearing",
        "manual_clearing_fail",
        "manual_mitigating",
        "manual_starting",
        "manual_starting_fail",
        "mitigating",
        "start_wait",
        "starting",
        "starting_fail",
    ] = FieldInfo(alias="AlarmState")
    """
    '#/components/schemas/BlackholePortSerializer/properties/AlarmState'
    "$.components.schemas.BlackholePortSerializer.properties.AlarmState"
    """

    alert_duration: str = FieldInfo(alias="AlertDuration")
    """
    '#/components/schemas/BlackholePortSerializer/properties/AlertDuration'
    "$.components.schemas.BlackholePortSerializer.properties.AlertDuration"
    """

    destination_ip: str = FieldInfo(alias="DestinationIP")
    """
    '#/components/schemas/BlackholePortSerializer/properties/DestinationIP'
    "$.components.schemas.BlackholePortSerializer.properties.DestinationIP"
    """

    id: int = FieldInfo(alias="ID")
    """
    '#/components/schemas/BlackholePortSerializer/properties/ID'
    "$.components.schemas.BlackholePortSerializer.properties.ID"
    """


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


class InstanceIsolation(BaseModel):
    reason: Optional[str] = None
    """
    '#/components/schemas/IsolationSerializer/properties/reason/anyOf/0'
    "$.components.schemas.IsolationSerializer.properties.reason.anyOf[0]"
    """


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

    keypair_name: Optional[str] = None
    """
    '#/components/schemas/InstanceSerializer/properties/keypair_name/anyOf/0'
    "$.components.schemas.InstanceSerializer.properties.keypair_name.anyOf[0]"
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
