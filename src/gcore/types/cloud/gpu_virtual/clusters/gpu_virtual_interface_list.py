# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .gpu_virtual_interface import GPUVirtualInterface

__all__ = ["GPUVirtualInterfaceList"]


class GPUVirtualInterfaceList(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUVirtualInterface]
    """Objects"""
