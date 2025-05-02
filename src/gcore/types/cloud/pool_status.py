# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .member_status import MemberStatus
from .provisioning_status import ProvisioningStatus
from .health_monitor_status import HealthMonitorStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["PoolStatus"]


class PoolStatus(BaseModel):
    id: str
    """UUID of the entity"""

    members: List[MemberStatus]
    """Members (servers) of the pool"""

    name: str
    """Name of the load balancer pool"""

    operating_status: LoadBalancerOperatingStatus
    """Operating status of the entity"""

    provisioning_status: ProvisioningStatus
    """Provisioning status of the entity"""

    health_monitor: Optional[HealthMonitorStatus] = None
    """Health Monitor of the Pool"""
