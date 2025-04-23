# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..neutron_route_param import NeutronRouteParam

__all__ = ["RouterUpdateParams", "ExternalGatewayInfo"]


class RouterUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Frouters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Brouter_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/routers/{project_id}/{region_id}/{router_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Frouters%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Brouter_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v1/routers/{project_id}/{region_id}/{router_id}'].patch.parameters[1].schema"
    """

    external_gateway_info: Optional[ExternalGatewayInfo]
    """
    '#/components/schemas/PatchRouterSerializer/properties/external_gateway_info/anyOf/0'
    "$.components.schemas.PatchRouterSerializer.properties.external_gateway_info.anyOf[0]"
    """

    name: Optional[str]
    """
    '#/components/schemas/PatchRouterSerializer/properties/name/anyOf/0'
    "$.components.schemas.PatchRouterSerializer.properties.name.anyOf[0]"
    """

    routes: Optional[Iterable[NeutronRouteParam]]
    """
    '#/components/schemas/PatchRouterSerializer/properties/routes/anyOf/0'
    "$.components.schemas.PatchRouterSerializer.properties.routes.anyOf[0]"
    """


class ExternalGatewayInfo(TypedDict, total=False):
    network_id: Required[str]
    """
    '#/components/schemas/RouterExternalManualGwSerializer/properties/network_id'
    "$.components.schemas.RouterExternalManualGwSerializer.properties.network_id"
    """

    enable_snat: bool
    """
    '#/components/schemas/RouterExternalManualGwSerializer/properties/enable_snat'
    "$.components.schemas.RouterExternalManualGwSerializer.properties.enable_snat"
    """

    type: Literal["manual"]
    """
    '#/components/schemas/RouterExternalManualGwSerializer/properties/type'
    "$.components.schemas.RouterExternalManualGwSerializer.properties.type"
    """
