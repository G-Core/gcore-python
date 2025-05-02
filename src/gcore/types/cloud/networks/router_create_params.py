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

    region_id: int

    name: Required[str]
    """name of router"""

    external_gateway_info: Optional[ExternalGatewayInfo]

    interfaces: Optional[Iterable[Interface]]
    """List of interfaces to attach to router immediately after creation."""

    routes: Optional[Iterable[Route]]
    """List of custom routes."""


class ExternalGatewayInfoRouterExternalManualGwSerializer(TypedDict, total=False):
    network_id: Required[str]
    """id of the external network."""

    enable_snat: bool
    """Is SNAT enabled. Defaults to true."""

    type: Literal["manual"]
    """must be 'manual'."""


class ExternalGatewayInfoRouterExternalDefaultGwSerializer(TypedDict, total=False):
    enable_snat: bool
    """Is SNAT enabled. Defaults to true."""

    type: Literal["default"]
    """must be 'default'."""


ExternalGatewayInfo: TypeAlias = Union[
    ExternalGatewayInfoRouterExternalManualGwSerializer, ExternalGatewayInfoRouterExternalDefaultGwSerializer
]


class Interface(TypedDict, total=False):
    subnet_id: Required[str]
    """id of the subnet to attach to."""

    type: Literal["subnet"]
    """must be 'subnet'."""


class Route(TypedDict, total=False):
    destination: Required[str]
    """CIDR of destination IPv4 subnet."""

    nexthop: Required[str]
    """
    IPv4 address to forward traffic to if it's destination IP matches 'destination'
    CIDR.
    """
