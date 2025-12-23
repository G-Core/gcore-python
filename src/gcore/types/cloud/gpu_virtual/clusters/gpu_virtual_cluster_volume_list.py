# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .gpu_virtual_cluster_volume import GPUVirtualClusterVolume

__all__ = ["GPUVirtualClusterVolumeList"]


class GPUVirtualClusterVolumeList(BaseModel):
    count: int
    """Number of objects"""

    results: List[GPUVirtualClusterVolume]
    """Objects"""
