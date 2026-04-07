# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .baremetal_image import BaremetalImage

__all__ = ["BaremetalImageList"]


class BaremetalImageList(BaseModel):
    count: int
    """Number of objects"""

    results: List[BaremetalImage]
    """Objects"""
