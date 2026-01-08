# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel
from .k8s_cluster_pool import K8SClusterPool

__all__ = ["PoolListResponse"]


class PoolListResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[K8SClusterPool]
    """Objects"""
