# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PoolCreateParams"]


class PoolCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    flavor_id: Required[str]
    """Flavor ID"""

    min_node_count: Required[int]
    """Minimum node count"""

    name: Required[str]
    """Pool's name"""

    auto_healing_enabled: Optional[bool]
    """Enable auto healing"""

    boot_volume_size: Optional[int]
    """Boot volume size"""

    boot_volume_type: Optional[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
    """Boot volume type"""

    crio_config: Optional[Dict[str, str]]
    """Cri-o configuration for pool nodes"""

    is_public_ipv4: Optional[bool]
    """Enable public v4 address"""

    kubelet_config: Optional[Dict[str, str]]
    """Kubelet configuration for pool nodes"""

    labels: Optional[Dict[str, str]]
    """Labels applied to the cluster pool"""

    max_node_count: Optional[int]
    """Maximum node count"""

    servergroup_policy: Optional[Literal["affinity", "anti-affinity", "soft-anti-affinity"]]
    """Server group policy: anti-affinity, soft-anti-affinity or affinity"""

    taints: Optional[Dict[str, str]]
    """Taints applied to the cluster pool"""
