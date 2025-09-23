# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PoolUpdateParams"]


class PoolUpdateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    cluster_name: Required[str]

    auto_healing_enabled: Optional[bool]
    """Enable/disable auto healing"""

    labels: Optional[Dict[str, str]]
    """Labels applied to the cluster pool"""

    max_node_count: Optional[int]
    """Maximum node count"""

    min_node_count: Optional[int]
    """Minimum node count"""

    node_count: Optional[int]
    """This field is deprecated. Please use the cluster pool resize handler instead."""

    taints: Optional[Dict[str, str]]
    """Taints applied to the cluster pool"""
