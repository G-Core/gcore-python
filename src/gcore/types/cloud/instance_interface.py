# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from .subnet import Subnet
from ..._models import BaseModel
from .floating_ip import FloatingIP

__all__ = ["InstanceInterface", "AllowedAddressPair", "IPAssignment", "NetworkDetails"]


class AllowedAddressPair(BaseModel):
    ip_address: str
    """
    '#/components/schemas/AllowedAddressPairsSerializer/properties/ip_address/anyOf/0'
    "$.components.schemas.AllowedAddressPairsSerializer.properties.ip_address.anyOf[0]"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/AllowedAddressPairsSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.AllowedAddressPairsSerializer.properties.mac_address.anyOf[0]"
    """


class IPAssignment(BaseModel):
    ip_address: str
    """
    '#/components/schemas/PortIpSubnetIdSerializer/properties/ip_address'
    "$.components.schemas.PortIpSubnetIdSerializer.properties.ip_address"
    """

    subnet_id: str
    """
    '#/components/schemas/PortIpSubnetIdSerializer/properties/subnet_id'
    "$.components.schemas.PortIpSubnetIdSerializer.properties.subnet_id"
    """


class NetworkDetails(BaseModel):
    id: str
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/id'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/created_at'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.created_at"
    """

    external: bool
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/external'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.external"
    """

    name: str
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/name'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.name"
    """

    port_security_enabled: bool
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/port_security_enabled'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.port_security_enabled"
    """

    region: str
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/region'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/region_id'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.region_id"
    """

    shared: bool
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/shared'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.shared"
    """

    tags: List[Tag]
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/tags'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.tags"
    """

    type: str
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/type'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.type"
    """

    updated_at: datetime
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/updated_at'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.updated_at"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.creator_task_id.anyOf[0]"
    """

    default: Optional[bool] = None
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/default/anyOf/0'
    "$.components.schemas.NetworkSubnetworkSerializer.properties['default'].anyOf[0]"
    """

    mtu: Optional[int] = None
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/mtu'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.mtu"
    """

    project_id: Optional[int] = None
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/project_id/anyOf/0'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.project_id.anyOf[0]"
    """

    segmentation_id: Optional[int] = None
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/segmentation_id/anyOf/0'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.segmentation_id.anyOf[0]"
    """

    subnets: Optional[List[Subnet]] = None
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/subnets/anyOf/0'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.subnets.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/NetworkSubnetworkSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.NetworkSubnetworkSerializer.properties.task_id.anyOf[0]"
    """


class InstanceInterface(BaseModel):
    allowed_address_pairs: List[AllowedAddressPair]
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/allowed_address_pairs'
    "$.components.schemas.InstanceInterfaceSerializer.properties.allowed_address_pairs"
    """

    floatingip_details: List[FloatingIP]
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/floatingip_details'
    "$.components.schemas.InstanceInterfaceSerializer.properties.floatingip_details"
    """

    ip_assignments: List[IPAssignment]
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/ip_assignments'
    "$.components.schemas.InstanceInterfaceSerializer.properties.ip_assignments"
    """

    network_details: NetworkDetails
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/network_details'
    "$.components.schemas.InstanceInterfaceSerializer.properties.network_details"
    """

    network_id: str
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/network_id'
    "$.components.schemas.InstanceInterfaceSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/port_id'
    "$.components.schemas.InstanceInterfaceSerializer.properties.port_id"
    """

    port_security_enabled: bool
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/port_security_enabled'
    "$.components.schemas.InstanceInterfaceSerializer.properties.port_security_enabled"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceInterfaceSerializer.properties.interface_name.anyOf[0]"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.InstanceInterfaceSerializer.properties.mac_address.anyOf[0]"
    """
