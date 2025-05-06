# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .load_balancer_listener_detail import LoadBalancerListenerDetail

__all__ = ["LoadBalancerListenerList"]


class LoadBalancerListenerList(BaseModel):
    count: int
    """Number of objects"""

    results: List[LoadBalancerListenerDetail]
    """Objects"""
