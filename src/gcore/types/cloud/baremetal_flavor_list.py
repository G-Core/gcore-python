# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .baremetal_flavor import BaremetalFlavor

__all__ = ["BaremetalFlavorList"]


class BaremetalFlavorList(BaseModel):
    count: int
    """Number of objects"""

    results: List[BaremetalFlavor]
    """Objects"""
