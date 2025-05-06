# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .load_balancer_flavor_detail import LoadBalancerFlavorDetail

__all__ = ["LoadBalancerFlavorList"]


class LoadBalancerFlavorList(BaseModel):
    count: int
    """Number of objects"""

    results: List[LoadBalancerFlavorDetail]
    """Objects"""
