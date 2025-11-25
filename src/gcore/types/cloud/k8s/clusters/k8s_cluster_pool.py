# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ....._models import BaseModel

__all__ = ["K8SClusterPool"]


class K8SClusterPool(BaseModel):
    id: str
    """UUID of the cluster pool"""

    auto_healing_enabled: bool
    """Indicates the status of auto healing"""

    boot_volume_size: int
    """Size of the boot volume"""

    boot_volume_type: str
    """Type of the boot volume"""

    created_at: str
    """Date of function creation"""

    crio_config: Dict[str, str]
    """Crio configuration for pool nodes"""

    flavor_id: str
    """ID of the cluster pool flavor"""

    is_public_ipv4: bool
    """Indicates if the pool is public"""

    kubelet_config: Dict[str, str]
    """Kubelet configuration for pool nodes"""

    labels: Dict[str, str]
    """Labels applied to the cluster pool"""

    max_node_count: int
    """Maximum node count in the cluster pool"""

    min_node_count: int
    """Minimum node count in the cluster pool"""

    name: str
    """Name of the cluster pool"""

    node_count: int
    """Node count in the cluster pool"""

    status: str
    """Status of the cluster pool"""

    taints: Dict[str, str]
    """Taints applied to the cluster pool"""

    servergroup_id: Optional[str] = None
    """Server group ID"""

    servergroup_name: Optional[str] = None
    """Server group name"""

    servergroup_policy: Optional[str] = None
    """Anti-affinity, affinity or soft-anti-affinity server group policy"""
