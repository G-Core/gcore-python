# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RouterUpdateParams", "ExternalGatewayInfo", "Route"]


class RouterUpdateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    external_gateway_info: Optional[ExternalGatewayInfo]
    """New external gateway configuration.

    Only type 'manual' is accepted on update, so you must provide the `network_id`
    of the external network. Set to null to remove the external gateway.
    """

    name: Optional[str]
    """New name of router"""

    routes: Optional[Iterable[Route]]
    """List of custom routes."""


class ExternalGatewayInfo(TypedDict, total=False):
    """New external gateway configuration.

    Only type 'manual' is accepted on update, so you must provide the `network_id` of the external network. Set to null to remove the external gateway.
    """

    network_id: Required[str]
    """ID of the external network to connect the router to."""

    enable_snat: bool
    """Is SNAT enabled. Defaults to true."""

    type: Literal["manual"]
    """Gateway type.

    Use 'manual' to explicitly specify which external network the router connects to
    via `network_id`. Required for PATCH/update operations.
    """


class Route(TypedDict, total=False):
    destination: Required[str]
    """CIDR of destination IPv4 or IPv6 subnet."""

    nexthop: Required[str]
    """
    IPv4 or IPv6 address to forward traffic to if it's destination IP matches
    'destination' CIDR.
    """
