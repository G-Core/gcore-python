# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .gpu_baremetal_flavor import GPUBaremetalFlavor

__all__ = ["GPUBaremetalFlavorList"]


class GPUBaremetalFlavorList(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUBaremetalFlavor]
    """Objects"""
