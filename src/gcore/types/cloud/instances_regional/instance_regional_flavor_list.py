# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .instance_regional_flavor_detailed import InstanceRegionalFlavorDetailed

__all__ = ["InstanceRegionalFlavorList"]


class InstanceRegionalFlavorList(BaseModel):
    count: int
    """Number of objects"""

    results: List[InstanceRegionalFlavorDetailed]
    """Objects"""
