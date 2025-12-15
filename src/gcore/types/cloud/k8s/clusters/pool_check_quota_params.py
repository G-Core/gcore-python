# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PoolCheckQuotaParams"]


class PoolCheckQuotaParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    flavor_id: Required[str]
    """Flavor ID"""

    boot_volume_size: Optional[int]
    """Boot volume size"""

    max_node_count: Optional[int]
    """Maximum node count"""

    min_node_count: Optional[int]
    """Minimum node count"""

    name: Optional[str]
    """Name of the cluster pool"""

    node_count: Optional[int]
    """Maximum node count"""

    servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]]
    """Server group policy: anti-affinity, soft-anti-affinity or affinity"""
