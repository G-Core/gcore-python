# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .gpu_baremetal_cluster_server import GPUBaremetalClusterServer

__all__ = ["GPUBaremetalClusterServerList"]


class GPUBaremetalClusterServerList(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUBaremetalClusterServer]
    """Objects"""
