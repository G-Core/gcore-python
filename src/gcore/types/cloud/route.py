# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Route"]


class Route(BaseModel):
    destination: str
    """CIDR of destination IPv4 subnet."""

    nexthop: str
    """
    IPv4 address to forward traffic to if it's destination IP matches 'destination'
    CIDR.
    """
