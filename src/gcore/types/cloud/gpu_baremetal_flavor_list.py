# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .gpu_baremetal_flavor import GPUBaremetalFlavor

__all__ = ["GPUBaremetalFlavorList"]


class GPUBaremetalFlavorList(BaseModel):
    count: int
    """
    '#/components/schemas/ListGpuBaremetalFlavorSerializer/properties/count'
    "$.components.schemas.ListGpuBaremetalFlavorSerializer.properties.count"
    """

    results: List[GPUBaremetalFlavor]
    """
    '#/components/schemas/ListGpuBaremetalFlavorSerializer/properties/results'
    "$.components.schemas.ListGpuBaremetalFlavorSerializer.properties.results"
    """
