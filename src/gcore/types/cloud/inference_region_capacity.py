# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["InferenceRegionCapacity", "Capacity"]


class Capacity(BaseModel):
    capacity: int
    """Available capacity."""

    flavor_name: str
    """Flavor name."""


class InferenceRegionCapacity(BaseModel):
    capacity: List[Capacity]
    """List of capacities by flavor."""

    region_id: int
    """Region ID."""
