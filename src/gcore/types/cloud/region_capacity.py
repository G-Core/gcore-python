# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .capacity import Capacity
from ..._models import BaseModel

__all__ = ["RegionCapacity"]


class RegionCapacity(BaseModel):
    capacity: List[Capacity]
    """List of capacities by flavor."""

    region_id: int
    """Region ID."""
