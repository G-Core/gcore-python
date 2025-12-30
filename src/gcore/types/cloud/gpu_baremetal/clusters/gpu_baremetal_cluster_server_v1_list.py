# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .gpu_baremetal_cluster_server_v1 import GPUBaremetalClusterServerV1

__all__ = ["GPUBaremetalClusterServerV1List"]


class GPUBaremetalClusterServerV1List(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUBaremetalClusterServerV1]
    """Objects"""
