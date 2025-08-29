# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .k8s_cluster import K8sCluster

__all__ = ["K8sClusterList"]


class K8sClusterList(BaseModel):
    count: int
    """Number of objects"""

    results: List[K8sCluster]
    """Objects"""
