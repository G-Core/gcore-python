# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .lifecycle_policy import LifecyclePolicy

__all__ = ["LifecyclePolicyListResponse"]


class LifecyclePolicyListResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[LifecyclePolicy]
    """Objects"""
