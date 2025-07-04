# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .inference_region_capacity import InferenceRegionCapacity

__all__ = ["InferenceRegionCapacityList"]


class InferenceRegionCapacityList(BaseModel):
    count: int
    """Number of objects"""

    results: List[InferenceRegionCapacity]
    """Objects"""
