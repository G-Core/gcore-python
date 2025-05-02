# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .gpu_cluster_server import GPUClusterServer

__all__ = ["GPUClusterServerList"]


class GPUClusterServerList(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUClusterServer]
    """Objects"""
