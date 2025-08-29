# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .k8s_cluster_version import K8sClusterVersion

__all__ = ["K8sClusterVersionList"]


class K8sClusterVersionList(BaseModel):
    count: int
    """Number of objects"""

    results: List[K8sClusterVersion]
    """Objects"""
