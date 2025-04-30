# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .gpu_cluster_server import GPUClusterServer

__all__ = ["GPUClusterServerList"]


class GPUClusterServerList(BaseModel):
    count: int
    """
    '#/components/schemas/GPUClusterServerCollectionSerializer/properties/count'
    "$.components.schemas.GPUClusterServerCollectionSerializer.properties.count"
    """

    results: List[GPUClusterServer]
    """
    '#/components/schemas/GPUClusterServerCollectionSerializer/properties/results'
    "$.components.schemas.GPUClusterServerCollectionSerializer.properties.results"
    """
