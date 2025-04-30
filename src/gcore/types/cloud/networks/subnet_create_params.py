# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..ip_version import IPVersion
from ..tag_update_list_param import TagUpdateListParam

__all__ = ["SubnetCreateParams", "HostRoute"]


class SubnetCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    cidr: Required[str]
    """
    '#/components/schemas/CreateSubnetSerializer/properties/cidr'
    "$.components.schemas.CreateSubnetSerializer.properties.cidr"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateSubnetSerializer/properties/name'
    "$.components.schemas.CreateSubnetSerializer.properties.name"
    """

    network_id: Required[str]
    """
    '#/components/schemas/CreateSubnetSerializer/properties/network_id'
    "$.components.schemas.CreateSubnetSerializer.properties.network_id"
    """

    connect_to_network_router: bool
    """
    '#/components/schemas/CreateSubnetSerializer/properties/connect_to_network_router'
    "$.components.schemas.CreateSubnetSerializer.properties.connect_to_network_router"
    """

    dns_nameservers: Optional[List[str]]
    """
    '#/components/schemas/CreateSubnetSerializer/properties/dns_nameservers/anyOf/0'
    "$.components.schemas.CreateSubnetSerializer.properties.dns_nameservers.anyOf[0]"
    """

    enable_dhcp: bool
    """
    '#/components/schemas/CreateSubnetSerializer/properties/enable_dhcp'
    "$.components.schemas.CreateSubnetSerializer.properties.enable_dhcp"
    """

    gateway_ip: Optional[str]
    """
    '#/components/schemas/CreateSubnetSerializer/properties/gateway_ip/anyOf/0'
    "$.components.schemas.CreateSubnetSerializer.properties.gateway_ip.anyOf[0]"
    """

    host_routes: Optional[Iterable[HostRoute]]
    """
    '#/components/schemas/CreateSubnetSerializer/properties/host_routes/anyOf/0'
    "$.components.schemas.CreateSubnetSerializer.properties.host_routes.anyOf[0]"
    """

    ip_version: IPVersion
    """
    '#/components/schemas/CreateSubnetSerializer/properties/ip_version'
    "$.components.schemas.CreateSubnetSerializer.properties.ip_version"
    """

    router_id_to_connect: Optional[str]
    """
    '#/components/schemas/CreateSubnetSerializer/properties/router_id_to_connect/anyOf/0'
    "$.components.schemas.CreateSubnetSerializer.properties.router_id_to_connect.anyOf[0]"
    """

    tags: TagUpdateListParam
    """
    '#/components/schemas/CreateSubnetSerializer/properties/tags'
    "$.components.schemas.CreateSubnetSerializer.properties.tags"
    """


class HostRoute(TypedDict, total=False):
    destination: Required[str]
    """
    '#/components/schemas/RouteInSerializer/properties/destination'
    "$.components.schemas.RouteInSerializer.properties.destination"
    """

    nexthop: Required[str]
    """
    '#/components/schemas/RouteInSerializer/properties/nexthop'
    "$.components.schemas.RouteInSerializer.properties.nexthop"
    """
