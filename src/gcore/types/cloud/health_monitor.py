# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .http_method import HTTPMethod
from .provisioning_status import ProvisioningStatus
from .lb_health_monitor_type import LbHealthMonitorType
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["HealthMonitor"]


class HealthMonitor(BaseModel):
    id: str
    """Health monitor ID"""

    admin_state_up: bool
    """Administrative state of the resource.

    When set to true, the resource is enabled and operational. When set to false,
    the resource is disabled and will not process traffic. When null is passed, the
    value is skipped and defaults to true.
    """

    delay: int
    """The time, in seconds, between sending probes to members"""

    max_retries: int
    """Number of successes before the member is switched to ONLINE state"""

    max_retries_down: int
    """Number of failures before the member is switched to ERROR state"""

    operating_status: LoadBalancerOperatingStatus
    """Health Monitor operating status"""

    provisioning_status: ProvisioningStatus
    """Health monitor lifecycle status"""

    timeout: int
    """The maximum time to connect. Must be less than the delay value"""

    type: LbHealthMonitorType
    """Health monitor type. Once health monitor is created, cannot be changed."""

    expected_codes: Optional[str] = None
    """Expected HTTP response codes.

    Can be a single code or a range of codes. Can only be used together with `HTTP`
    or `HTTPS` health monitor type. For example,
    200,202,300-302,401,403,404,500-504. If not specified, the default is 200.
    """

    http_method: Optional[HTTPMethod] = None
    """HTTP method"""

    url_path: Optional[str] = None
    """URL Path. Defaults to '/'"""
