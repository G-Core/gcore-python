# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from .subnet import Subnet
from ..._models import BaseModel
from .floating_ip import FloatingIP

__all__ = [
    "NetworkInterface",
    "AllowedAddressPair",
    "IPAssignment",
    "NetworkDetails",
    "SubPort",
    "SubPortAllowedAddressPair",
    "SubPortIPAssignment",
    "SubPortNetworkDetails",
]


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


class SubPortAllowedAddressPair(BaseModel):
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


class SubPortIPAssignment(BaseModel):
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


class SubPortNetworkDetails(BaseModel):
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


class SubPort(BaseModel):
    allowed_address_pairs: List[SubPortAllowedAddressPair]
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/allowed_address_pairs'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.allowed_address_pairs"
    """

    floatingip_details: List[FloatingIP]
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/floatingip_details'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.floatingip_details"
    """

    ip_assignments: List[SubPortIPAssignment]
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/ip_assignments'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.ip_assignments"
    """

    network_details: SubPortNetworkDetails
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/network_details'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.network_details"
    """

    network_id: str
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/network_id'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/port_id'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.port_id"
    """

    port_security_enabled: bool
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/port_security_enabled'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.port_security_enabled"
    """

    segmentation_id: int
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/segmentation_id'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.segmentation_id"
    """

    segmentation_type: str
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/segmentation_type'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.segmentation_type"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.interface_name.anyOf[0]"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceSubportSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.InstanceInterfaceSubportSerializer.properties.mac_address.anyOf[0]"
    """


class NetworkInterface(BaseModel):
    allowed_address_pairs: List[AllowedAddressPair]
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/allowed_address_pairs'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.allowed_address_pairs"
    """

    floatingip_details: List[FloatingIP]
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/floatingip_details'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.floatingip_details"
    """

    ip_assignments: List[IPAssignment]
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/ip_assignments'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.ip_assignments"
    """

    network_details: NetworkDetails
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/network_details'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.network_details"
    """

    network_id: str
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/network_id'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/port_id'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.port_id"
    """

    port_security_enabled: bool
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/port_security_enabled'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.port_security_enabled"
    """

    sub_ports: List[SubPort]
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/sub_ports'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.sub_ports"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.interface_name.anyOf[0]"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/InstanceInterfaceTrunkSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.InstanceInterfaceTrunkSerializer.properties.mac_address.anyOf[0]"
    """
