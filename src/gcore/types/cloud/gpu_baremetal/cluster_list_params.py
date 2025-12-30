# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ClusterListParams"]


class ClusterListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    limit: int
    """Limit of items on a single page"""

    managed_by: List[Literal["k8s", "user"]]
    """Specifies the entity responsible for managing the resource.

    - `user`: The resource (cluster) is created and maintained directly by the user.
    - `k8s`: The resource is created and maintained automatically by Managed
      Kubernetes service
    """

    offset: int
    """Offset in results list"""
