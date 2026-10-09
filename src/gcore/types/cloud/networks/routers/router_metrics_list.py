# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .router_metrics import RouterMetrics

__all__ = ["RouterMetricsList"]


class RouterMetricsList(BaseModel):
    count: int
    """Number of objects"""

    results: List[RouterMetrics]
    """Objects"""
