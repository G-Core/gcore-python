# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Route"]


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
