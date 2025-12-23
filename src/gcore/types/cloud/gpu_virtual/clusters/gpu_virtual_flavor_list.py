# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .gpu_virtual_flavor import GPUVirtualFlavor

__all__ = ["GPUVirtualFlavorList"]


class GPUVirtualFlavorList(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUVirtualFlavor]
    """Objects"""
