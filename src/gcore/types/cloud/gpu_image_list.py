# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .gpu_image import GPUImage

__all__ = ["GPUImageList"]


class GPUImageList(BaseModel):
    count: int
    """
    '#/components/schemas/ListGpuImageSerializer/properties/count'
    "$.components.schemas.ListGpuImageSerializer.properties.count"
    """

    results: List[GPUImage]
    """
    '#/components/schemas/ListGpuImageSerializer/properties/results'
    "$.components.schemas.ListGpuImageSerializer.properties.results"
    """
