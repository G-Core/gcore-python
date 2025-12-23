# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .gpu_virtual_cluster_server import GPUVirtualClusterServer

__all__ = ["GPUVirtualClusterServerList"]


class GPUVirtualClusterServerList(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUVirtualClusterServer]
    """Objects"""
