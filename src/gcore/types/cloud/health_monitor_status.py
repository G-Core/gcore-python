# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .health_monitor_type import HealthMonitorType
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["HealthMonitorStatus"]


class HealthMonitorStatus(BaseModel):
    id: str
    """UUID of the entity"""

    operating_status: LoadBalancerOperatingStatus
    """Operating status of the entity"""

    provisioning_status: ProvisioningStatus
    """Provisioning status of the entity"""

    type: HealthMonitorType
    """Type of the Health Monitor"""
