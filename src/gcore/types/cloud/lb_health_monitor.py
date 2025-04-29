# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .http_method import HTTPMethod
from .health_monitor_type import HealthMonitorType
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["LbHealthMonitor"]


class LbHealthMonitor(BaseModel):
    id: str
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/id'
    "$.components.schemas.LbHealthMonitorSerializer.properties.id"
    """

    admin_state_up: bool
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/admin_state_up'
    "$.components.schemas.LbHealthMonitorSerializer.properties.admin_state_up"
    """

    delay: int
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/delay'
    "$.components.schemas.LbHealthMonitorSerializer.properties.delay"
    """

    max_retries: int
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/max_retries'
    "$.components.schemas.LbHealthMonitorSerializer.properties.max_retries"
    """

    max_retries_down: int
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/max_retries_down'
    "$.components.schemas.LbHealthMonitorSerializer.properties.max_retries_down"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/operating_status'
    "$.components.schemas.LbHealthMonitorSerializer.properties.operating_status"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/provisioning_status'
    "$.components.schemas.LbHealthMonitorSerializer.properties.provisioning_status"
    """

    timeout: int
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/timeout'
    "$.components.schemas.LbHealthMonitorSerializer.properties.timeout"
    """

    type: HealthMonitorType
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/type'
    "$.components.schemas.LbHealthMonitorSerializer.properties.type"
    """

    expected_codes: Optional[str] = None
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/expected_codes/anyOf/0'
    "$.components.schemas.LbHealthMonitorSerializer.properties.expected_codes.anyOf[0]"
    """

    http_method: Optional[HTTPMethod] = None
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/http_method/anyOf/0'
    "$.components.schemas.LbHealthMonitorSerializer.properties.http_method.anyOf[0]"
    """

    url_path: Optional[str] = None
    """
    '#/components/schemas/LbHealthMonitorSerializer/properties/url_path/anyOf/0'
    "$.components.schemas.LbHealthMonitorSerializer.properties.url_path.anyOf[0]"
    """
