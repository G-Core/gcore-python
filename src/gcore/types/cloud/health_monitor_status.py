# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .provisioning_status import ProvisioningStatus
from .lb_health_monitor_type import LbHealthMonitorType
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["HealthMonitorStatus"]


class HealthMonitorStatus(BaseModel):
    id: str
    """UUID of the entity"""

    operating_status: LoadBalancerOperatingStatus
    """Operating status of the entity"""

    provisioning_status: ProvisioningStatus
    """Provisioning status of the entity"""

    type: LbHealthMonitorType
    """Type of the Health Monitor"""
