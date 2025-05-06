# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .load_balancer_metrics import LoadBalancerMetrics

__all__ = ["LoadBalancerMetricsList"]


class LoadBalancerMetricsList(BaseModel):
    count: int
    """Number of objects"""

    results: List[LoadBalancerMetrics]
    """Objects"""
