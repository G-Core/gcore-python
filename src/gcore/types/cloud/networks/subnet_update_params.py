# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SubnetUpdateParams", "HostRoute"]


class SubnetUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Fsubnets%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bsubnet_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v1/subnets/{project_id}/{region_id}/{subnet_id}'].patch.parameters[1].schema"
    """

    dns_nameservers: Optional[List[str]]
    """
    '#/components/schemas/PatchSubnetSerializer/properties/dns_nameservers/anyOf/0'
    "$.components.schemas.PatchSubnetSerializer.properties.dns_nameservers.anyOf[0]"
    """

    enable_dhcp: Optional[bool]
    """
    '#/components/schemas/PatchSubnetSerializer/properties/enable_dhcp/anyOf/0'
    "$.components.schemas.PatchSubnetSerializer.properties.enable_dhcp.anyOf[0]"
    """

    gateway_ip: Optional[str]
    """
    '#/components/schemas/PatchSubnetSerializer/properties/gateway_ip/anyOf/0'
    "$.components.schemas.PatchSubnetSerializer.properties.gateway_ip.anyOf[0]"
    """

    host_routes: Optional[Iterable[HostRoute]]
    """
    '#/components/schemas/PatchSubnetSerializer/properties/host_routes/anyOf/0'
    "$.components.schemas.PatchSubnetSerializer.properties.host_routes.anyOf[0]"
    """

    name: Optional[str]
    """
    '#/components/schemas/PatchSubnetSerializer/properties/name/anyOf/0'
    "$.components.schemas.PatchSubnetSerializer.properties.name.anyOf[0]"
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
