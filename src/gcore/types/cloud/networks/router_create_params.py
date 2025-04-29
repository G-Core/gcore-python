# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "RouterCreateParams",
    "ExternalGatewayInfo",
    "ExternalGatewayInfoRouterExternalManualGwSerializer",
    "ExternalGatewayInfoRouterExternalDefaultGwSerializer",
    "Interface",
    "Route",
]


class RouterCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Frouters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/routers/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Frouters%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/routers/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateRouterSerializer/properties/name'
    "$.components.schemas.CreateRouterSerializer.properties.name"
    """

    external_gateway_info: Optional[ExternalGatewayInfo]
    """
    '#/components/schemas/CreateRouterSerializer/properties/external_gateway_info'
    "$.components.schemas.CreateRouterSerializer.properties.external_gateway_info"
    """

    interfaces: Optional[Iterable[Interface]]
    """
    '#/components/schemas/CreateRouterSerializer/properties/interfaces/anyOf/0'
    "$.components.schemas.CreateRouterSerializer.properties.interfaces.anyOf[0]"
    """

    routes: Optional[Iterable[Route]]
    """
    '#/components/schemas/CreateRouterSerializer/properties/routes/anyOf/0'
    "$.components.schemas.CreateRouterSerializer.properties.routes.anyOf[0]"
    """


class ExternalGatewayInfoRouterExternalManualGwSerializer(TypedDict, total=False):
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


class ExternalGatewayInfoRouterExternalDefaultGwSerializer(TypedDict, total=False):
    enable_snat: bool
    """
    '#/components/schemas/RouterExternalDefaultGwSerializer/properties/enable_snat'
    "$.components.schemas.RouterExternalDefaultGwSerializer.properties.enable_snat"
    """

    type: Literal["default"]
    """
    '#/components/schemas/RouterExternalDefaultGwSerializer/properties/type'
    "$.components.schemas.RouterExternalDefaultGwSerializer.properties.type"
    """


ExternalGatewayInfo: TypeAlias = Union[
    ExternalGatewayInfoRouterExternalManualGwSerializer, ExternalGatewayInfoRouterExternalDefaultGwSerializer
]


class Interface(TypedDict, total=False):
    subnet_id: Required[str]
    """
    '#/components/schemas/CreateRouterInterfaceSubnetSerializer/properties/subnet_id'
    "$.components.schemas.CreateRouterInterfaceSubnetSerializer.properties.subnet_id"
    """

    type: Literal["subnet"]
    """
    '#/components/schemas/CreateRouterInterfaceSubnetSerializer/properties/type'
    "$.components.schemas.CreateRouterInterfaceSubnetSerializer.properties.type"
    """


class Route(TypedDict, total=False):
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
