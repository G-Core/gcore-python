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
    """
    '#/components/schemas/PoolStatusSerializer/properties/id'
    "$.components.schemas.PoolStatusSerializer.properties.id"
    """

    members: List[MemberStatus]
    """
    '#/components/schemas/PoolStatusSerializer/properties/members'
    "$.components.schemas.PoolStatusSerializer.properties.members"
    """

    name: str
    """
    '#/components/schemas/PoolStatusSerializer/properties/name'
    "$.components.schemas.PoolStatusSerializer.properties.name"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/PoolStatusSerializer/properties/operating_status'
    "$.components.schemas.PoolStatusSerializer.properties.operating_status"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/PoolStatusSerializer/properties/provisioning_status'
    "$.components.schemas.PoolStatusSerializer.properties.provisioning_status"
    """

    health_monitor: Optional[HealthMonitorStatus] = None
    """
    '#/components/schemas/PoolStatusSerializer/properties/health_monitor'
    "$.components.schemas.PoolStatusSerializer.properties.health_monitor"
    """
