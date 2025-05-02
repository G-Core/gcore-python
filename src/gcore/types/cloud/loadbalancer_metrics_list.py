# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .loadbalancer_metrics import LoadbalancerMetrics

__all__ = ["LoadbalancerMetricsList"]


class LoadbalancerMetricsList(BaseModel):
    count: int
    """Number of objects"""

    results: List[LoadbalancerMetrics]
    """Objects"""
