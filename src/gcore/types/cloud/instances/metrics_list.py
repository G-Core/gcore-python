# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .metrics import Metrics
from ...._models import BaseModel

__all__ = ["MetricsList"]


class MetricsList(BaseModel):
    count: int
    """Number of objects"""

    results: List[Metrics]
    """Objects"""
