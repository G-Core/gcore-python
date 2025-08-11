# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DDOSProfileOptionList"]


class DDOSProfileOptionList(BaseModel):
    active: bool
    """
    Controls whether the DDoS protection profile is enabled and actively protecting
    the resource
    """

    bgp: bool
    """Enables Border Gateway Protocol (BGP) routing for DDoS protection traffic"""
