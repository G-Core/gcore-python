# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .load_balancer_l7_policy import LoadBalancerL7Policy

__all__ = ["LoadBalancerL7PolicyList"]


class LoadBalancerL7PolicyList(BaseModel):
    count: Optional[int] = None
    """Number of objects"""

    results: Optional[List[LoadBalancerL7Policy]] = None
    """Objects"""
