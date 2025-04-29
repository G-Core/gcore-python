# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .health_monitor_type import HealthMonitorType
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["HealthMonitorStatus"]


class HealthMonitorStatus(BaseModel):
    id: str
    """
    '#/components/schemas/HealthMonitorStatusSerializer/properties/id'
    "$.components.schemas.HealthMonitorStatusSerializer.properties.id"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/HealthMonitorStatusSerializer/properties/operating_status'
    "$.components.schemas.HealthMonitorStatusSerializer.properties.operating_status"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/HealthMonitorStatusSerializer/properties/provisioning_status'
    "$.components.schemas.HealthMonitorStatusSerializer.properties.provisioning_status"
    """

    type: HealthMonitorType
    """
    '#/components/schemas/HealthMonitorStatusSerializer/properties/type'
    "$.components.schemas.HealthMonitorStatusSerializer.properties.type"
    """
