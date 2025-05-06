# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .load_balancer_l7_rule import LoadBalancerL7Rule

__all__ = ["LoadBalancerL7RuleList"]


class LoadBalancerL7RuleList(BaseModel):
    count: Optional[int] = None
    """Number of objects"""

    results: Optional[List[LoadBalancerL7Rule]] = None
    """Objects"""
