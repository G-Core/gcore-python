# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .pool_status import PoolStatus
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["ListenerStatus"]


class ListenerStatus(BaseModel):
    id: str
    """UUID of the entity"""

    name: str
    """Name of the load balancer listener"""

    operating_status: LoadBalancerOperatingStatus
    """Operating status of the entity"""

    pools: List[PoolStatus]
    """Pools of the Listeners"""

    provisioning_status: ProvisioningStatus
    """Provisioning status of the entity"""
