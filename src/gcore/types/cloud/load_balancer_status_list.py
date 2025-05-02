# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .load_balancer_status import LoadBalancerStatus

__all__ = ["LoadBalancerStatusList"]


class LoadBalancerStatusList(BaseModel):
    count: int
    """Number of objects"""

    results: List[LoadBalancerStatus]
    """Objects"""
