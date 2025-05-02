# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .gpu_image import GPUImage

__all__ = ["GPUImageList"]


class GPUImageList(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUImage]
    """Objects"""
