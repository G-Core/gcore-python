# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .load_balancer_l7_rule import LoadBalancerL7Rule

__all__ = ["LoadBalancerL7RuleList"]


class LoadBalancerL7RuleList(BaseModel):
    count: int
    """Number of objects"""

    results: List[LoadBalancerL7Rule]
    """Objects"""
