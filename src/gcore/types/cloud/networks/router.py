# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "Router",
    "Interface",
    "InterfaceIPAssignment",
    "Route",
    "ExternalGatewayInfo",
    "ExternalGatewayInfoExternalFixedIP",
]


class InterfaceIPAssignment(BaseModel):
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


class Interface(BaseModel):
    ip_assignments: List[InterfaceIPAssignment]
    """
    '#/components/schemas/PortSerializer/properties/ip_assignments'
    "$.components.schemas.PortSerializer.properties.ip_assignments"
    """

    network_id: str
    """
    '#/components/schemas/PortSerializer/properties/network_id'
    "$.components.schemas.PortSerializer.properties.network_id"
    """

    port_id: str
    """
    '#/components/schemas/PortSerializer/properties/port_id'
    "$.components.schemas.PortSerializer.properties.port_id"
    """

    mac_address: Optional[str] = None
    """
    '#/components/schemas/PortSerializer/properties/mac_address/anyOf/0'
    "$.components.schemas.PortSerializer.properties.mac_address.anyOf[0]"
    """


class Route(BaseModel):
    destination: str
    """
    '#/components/schemas/RouteOutSerializer/properties/destination'
    "$.components.schemas.RouteOutSerializer.properties.destination"
    """

    nexthop: str
    """
    '#/components/schemas/RouteOutSerializer/properties/nexthop'
    "$.components.schemas.RouteOutSerializer.properties.nexthop"
    """


class ExternalGatewayInfoExternalFixedIP(BaseModel):
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


class ExternalGatewayInfo(BaseModel):
    enable_snat: bool
    """
    '#/components/schemas/ExternalGatewaySerializer/properties/enable_snat'
    "$.components.schemas.ExternalGatewaySerializer.properties.enable_snat"
    """

    external_fixed_ips: List[ExternalGatewayInfoExternalFixedIP]
    """
    '#/components/schemas/ExternalGatewaySerializer/properties/external_fixed_ips'
    "$.components.schemas.ExternalGatewaySerializer.properties.external_fixed_ips"
    """

    network_id: str
    """
    '#/components/schemas/ExternalGatewaySerializer/properties/network_id'
    "$.components.schemas.ExternalGatewaySerializer.properties.network_id"
    """


class Router(BaseModel):
    id: str
    """
    '#/components/schemas/RouterSerializer/properties/id'
    "$.components.schemas.RouterSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/RouterSerializer/properties/created_at'
    "$.components.schemas.RouterSerializer.properties.created_at"
    """

    distributed: bool
    """
    '#/components/schemas/RouterSerializer/properties/distributed'
    "$.components.schemas.RouterSerializer.properties.distributed"
    """

    interfaces: List[Interface]
    """
    '#/components/schemas/RouterSerializer/properties/interfaces'
    "$.components.schemas.RouterSerializer.properties.interfaces"
    """

    name: str
    """
    '#/components/schemas/RouterSerializer/properties/name'
    "$.components.schemas.RouterSerializer.properties.name"
    """

    project_id: int
    """
    '#/components/schemas/RouterSerializer/properties/project_id'
    "$.components.schemas.RouterSerializer.properties.project_id"
    """

    region: str
    """
    '#/components/schemas/RouterSerializer/properties/region'
    "$.components.schemas.RouterSerializer.properties.region"
    """

    region_id: int
    """
    '#/components/schemas/RouterSerializer/properties/region_id'
    "$.components.schemas.RouterSerializer.properties.region_id"
    """

    routes: List[Route]
    """
    '#/components/schemas/RouterSerializer/properties/routes'
    "$.components.schemas.RouterSerializer.properties.routes"
    """

    status: str
    """
    '#/components/schemas/RouterSerializer/properties/status'
    "$.components.schemas.RouterSerializer.properties.status"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/RouterSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.RouterSerializer.properties.task_id.anyOf[0]"
    """

    updated_at: datetime
    """
    '#/components/schemas/RouterSerializer/properties/updated_at'
    "$.components.schemas.RouterSerializer.properties.updated_at"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/RouterSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.RouterSerializer.properties.creator_task_id.anyOf[0]"
    """

    external_gateway_info: Optional[ExternalGatewayInfo] = None
    """
    '#/components/schemas/RouterSerializer/properties/external_gateway_info/anyOf/0'
    "$.components.schemas.RouterSerializer.properties.external_gateway_info.anyOf[0]"
    """
