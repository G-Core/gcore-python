# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["NeutronRoute"]


class NeutronRoute(BaseModel):
    destination: str
    """
    '#/components/schemas/NeutronRouteSerializer/properties/destination'
    "$.components.schemas.NeutronRouteSerializer.properties.destination"
    """

    nexthop: str
    """
    '#/components/schemas/NeutronRouteSerializer/properties/nexthop'
    "$.components.schemas.NeutronRouteSerializer.properties.nexthop"
    """
