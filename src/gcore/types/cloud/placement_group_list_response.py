# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .placement_group import PlacementGroup

__all__ = ["PlacementGroupListResponse"]


class PlacementGroupListResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[PlacementGroup]
    """Objects"""
