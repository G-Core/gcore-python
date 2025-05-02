# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .region_capacity import RegionCapacity

__all__ = ["RegionCapacityList"]


class RegionCapacityList(BaseModel):
    count: int
    """Number of objects"""

    results: List[RegionCapacity]
    """Objects"""
