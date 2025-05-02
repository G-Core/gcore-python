# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..tag import Tag
from ...._models import BaseModel
from ..ddos_profile import DDOSProfile
from ..blackhole_port import BlackholePort
from ..instance_isolation import InstanceIsolation
from .baremetal_fixed_address import BaremetalFixedAddress
from .baremetal_floating_address import BaremetalFloatingAddress

__all__ = ["BaremetalServer", "Address", "FixedIPAssignment", "Flavor", "FlavorHardwareDescription"]

Address: TypeAlias = Union[BaremetalFloatingAddress, BaremetalFixedAddress]


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


class Flavor(BaseModel):
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

    hardware_description: FlavorHardwareDescription
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


class BaremetalServer(BaseModel):
    addresses: Dict[str, List[Address]]
    """
    '#/components/schemas/BareMetalServerSerializer/properties/addresses'
    "$.components.schemas.BareMetalServerSerializer.properties.addresses"
    """

    blackhole_ports: List[BlackholePort]
    """
    '#/components/schemas/BareMetalServerSerializer/properties/blackhole_ports'
    "$.components.schemas.BareMetalServerSerializer.properties.blackhole_ports"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/BareMetalServerSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.BareMetalServerSerializer.properties.creator_task_id.anyOf[0]"
    """

    ddos_profile: Optional[DDOSProfile] = None
    """
    '#/components/schemas/BareMetalServerSerializer/properties/ddos_profile/anyOf/0'
    "$.components.schemas.BareMetalServerSerializer.properties.ddos_profile.anyOf[0]"
    """

    fixed_ip_assignments: List[FixedIPAssignment]
    """
    '#/components/schemas/BareMetalServerSerializer/properties/fixed_ip_assignments'
    "$.components.schemas.BareMetalServerSerializer.properties.fixed_ip_assignments"
    """

    flavor: Flavor
    """
    '#/components/schemas/BareMetalServerSerializer/properties/flavor'
    "$.components.schemas.BareMetalServerSerializer.properties.flavor"
    """

    instance_created: datetime
    """
    '#/components/schemas/BareMetalServerSerializer/properties/instance_created'
    "$.components.schemas.BareMetalServerSerializer.properties.instance_created"
    """

    instance_description: Optional[str] = None
    """
    '#/components/schemas/BareMetalServerSerializer/properties/instance_description/anyOf/0'
    "$.components.schemas.BareMetalServerSerializer.properties.instance_description.anyOf[0]"
    """

    instance_id: str
    """
    '#/components/schemas/BareMetalServerSerializer/properties/instance_id'
    "$.components.schemas.BareMetalServerSerializer.properties.instance_id"
    """

    instance_isolation: Optional[InstanceIsolation] = None
    """
    '#/components/schemas/BareMetalServerSerializer/properties/instance_isolation/anyOf/0'
    "$.components.schemas.BareMetalServerSerializer.properties.instance_isolation.anyOf[0]"
    """

    instance_name: str
    """
    '#/components/schemas/BareMetalServerSerializer/properties/instance_name'
    "$.components.schemas.BareMetalServerSerializer.properties.instance_name"
    """

    project_id: int
    """
    '#/components/schemas/BareMetalServerSerializer/properties/project_id'
    "$.components.schemas.BareMetalServerSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/BareMetalServerSerializer/properties/region'
    "$.components.schemas.BareMetalServerSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/BareMetalServerSerializer/properties/region_id'
    "$.components.schemas.BareMetalServerSerializer.properties.region_id"
    """

    ssh_key_name: Optional[str] = None
    """
    '#/components/schemas/BareMetalServerSerializer/properties/ssh_key_name/anyOf/0'
    "$.components.schemas.BareMetalServerSerializer.properties.ssh_key_name.anyOf[0]"
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
    '#/components/schemas/BareMetalServerSerializer/properties/status'
    "$.components.schemas.BareMetalServerSerializer.properties.status"
    """

    tags: List[Tag]
    """
    '#/components/schemas/BareMetalServerSerializer/properties/tags'
    "$.components.schemas.BareMetalServerSerializer.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/BareMetalServerSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.BareMetalServerSerializer.properties.task_id.anyOf[0]"
    """

    task_state: Optional[str] = None
    """
    '#/components/schemas/BareMetalServerSerializer/properties/task_state/anyOf/0'
    "$.components.schemas.BareMetalServerSerializer.properties.task_state.anyOf[0]"
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
    '#/components/schemas/BareMetalServerSerializer/properties/vm_state'
    "$.components.schemas.BareMetalServerSerializer.properties.vm_state"
    """
