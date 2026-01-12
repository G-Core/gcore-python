# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .instance_flavor_detailed import InstanceFlavorDetailed

__all__ = ["InstanceFlavorList"]


class InstanceFlavorList(BaseModel):
    count: int
    """Number of objects"""

    results: List[InstanceFlavorDetailed]
    """Objects"""
