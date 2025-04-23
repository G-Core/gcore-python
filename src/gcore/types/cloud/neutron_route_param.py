# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NeutronRouteParam"]


class NeutronRouteParam(TypedDict, total=False):
    destination: Required[str]
    """
    '#/components/schemas/NeutronRouteSerializer/properties/destination'
    "$.components.schemas.NeutronRouteSerializer.properties.destination"
    """

    nexthop: Required[str]
    """
    '#/components/schemas/NeutronRouteSerializer/properties/nexthop'
    "$.components.schemas.NeutronRouteSerializer.properties.nexthop"
    """
