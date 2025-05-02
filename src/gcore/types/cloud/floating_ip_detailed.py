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
    """
    '#/components/schemas/BaseFlavorSerializer/properties/flavor_id'
    "$.components.schemas.BaseFlavorSerializer.properties.flavor_id"
    """

    flavor_name: str
    """
    '#/components/schemas/BaseFlavorSerializer/properties/flavor_name'
    "$.components.schemas.BaseFlavorSerializer.properties.flavor_name"
    """

    ram: int
    """
    '#/components/schemas/BaseFlavorSerializer/properties/ram'
    "$.components.schemas.BaseFlavorSerializer.properties.ram"
    """

    vcpus: int
    """
    '#/components/schemas/BaseFlavorSerializer/properties/vcpus'
    "$.components.schemas.BaseFlavorSerializer.properties.vcpus"
    """


class InstanceSecurityGroup(BaseModel):
    name: str
    """
    '#/components/schemas/NameSerializerPydantic/properties/name'
    "$.components.schemas.NameSerializerPydantic.properties.name"
    """


class InstanceVolume(BaseModel):
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
    addresses: Dict[str, List[InstanceAddress]]
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/addresses'
    "$.components.schemas.InstanceInFloatingSerializer.properties.addresses"
    """

    creator_task_id: str
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/creator_task_id'
    "$.components.schemas.InstanceInFloatingSerializer.properties.creator_task_id"
    """

    flavor: InstanceFlavor
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/flavor'
    "$.components.schemas.InstanceInFloatingSerializer.properties.flavor"
    """

    instance_created: datetime
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/instance_created'
    "$.components.schemas.InstanceInFloatingSerializer.properties.instance_created"
    """

    instance_description: Optional[str] = None
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/instance_description/anyOf/0'
    "$.components.schemas.InstanceInFloatingSerializer.properties.instance_description.anyOf[0]"
    """

    instance_id: str
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/instance_id'
    "$.components.schemas.InstanceInFloatingSerializer.properties.instance_id"
    """

    instance_name: str
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/instance_name'
    "$.components.schemas.InstanceInFloatingSerializer.properties.instance_name"
    """

    project_id: int
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/project_id'
    "$.components.schemas.InstanceInFloatingSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/region'
    "$.components.schemas.InstanceInFloatingSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/region_id'
    "$.components.schemas.InstanceInFloatingSerializer.properties.region_id"
    """

    security_groups: List[InstanceSecurityGroup]
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/security_groups'
    "$.components.schemas.InstanceInFloatingSerializer.properties.security_groups"
    """

    ssh_key_name: Optional[str] = None
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/ssh_key_name/anyOf/0'
    "$.components.schemas.InstanceInFloatingSerializer.properties.ssh_key_name.anyOf[0]"
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
    '#/components/schemas/InstanceInFloatingSerializer/properties/status'
    "$.components.schemas.InstanceInFloatingSerializer.properties.status"
    """

    tags: List[Tag]
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/tags'
    "$.components.schemas.InstanceInFloatingSerializer.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.InstanceInFloatingSerializer.properties.task_id.anyOf[0]"
    """

    task_state: Optional[str] = None
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/task_state/anyOf/0'
    "$.components.schemas.InstanceInFloatingSerializer.properties.task_state.anyOf[0]"
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
    '#/components/schemas/InstanceInFloatingSerializer/properties/vm_state'
    "$.components.schemas.InstanceInFloatingSerializer.properties.vm_state"
    """

    volumes: List[InstanceVolume]
    """
    '#/components/schemas/InstanceInFloatingSerializer/properties/volumes'
    "$.components.schemas.InstanceInFloatingSerializer.properties.volumes"
    """


class FloatingIPDetailed(BaseModel):
    id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/id/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.id.anyOf[0]"
    """

    created_at: datetime
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/created_at'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.created_at"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.creator_task_id.anyOf[0]"
    """

    dns_domain: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/dns_domain/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.dns_domain.anyOf[0]"
    """

    dns_name: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/dns_name/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.dns_name.anyOf[0]"
    """

    fixed_ip_address: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/fixed_ip_address/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.fixed_ip_address.anyOf[0]"
    """

    floating_ip_address: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/floating_ip_address/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.floating_ip_address.anyOf[0]"
    """

    instance: Optional[Instance] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/instance/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.instance.anyOf[0]"
    """

    loadbalancer: Optional[LoadBalancer] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/loadbalancer/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.loadbalancer.anyOf[0]"
    """

    port_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/port_id/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.port_id.anyOf[0]"
    """

    project_id: int
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/project_id'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/region'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/region_id'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.region_id"
    """

    router_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/router_id/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.router_id.anyOf[0]"
    """

    status: Optional[FloatingIPStatus] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/status/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.status.anyOf[0]"
    """

    subnet_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/subnet_id/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.subnet_id.anyOf[0]"
    """

    tags: List[Tag]
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/tags'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.tags"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.task_id.anyOf[0]"
    """

    updated_at: datetime
    """
    '#/components/schemas/FloatingIPDetailedSerializer/properties/updated_at'
    "$.components.schemas.FloatingIPDetailedSerializer.properties.updated_at"
    """
