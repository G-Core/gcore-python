# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ...http_method import HTTPMethod
from ...lb_health_monitor_type import LbHealthMonitorType

__all__ = ["HealthMonitorCreateParams"]


class HealthMonitorCreateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    delay: Required[int]
    """The time, in seconds, between sending probes to members"""

    max_retries: Required[int]
    """Number of successes before the member is switched to ONLINE state"""

    api_timeout: Required[Annotated[int, PropertyInfo(alias="timeout")]]
    """The maximum time to connect. Must be less than the delay value"""

    type: Required[LbHealthMonitorType]
    """Health monitor type. Once health monitor is created, cannot be changed."""

    expected_codes: Optional[str]
    """Expected HTTP response codes.

    Can be a single code or a range of codes. Can only be used together with `HTTP`
    or `HTTPS` health monitor type. For example,
    200,202,300-302,401,403,404,500-504. If not specified, the default is 200.
    """

    http_method: Optional[HTTPMethod]
    """HTTP method.

    Can only be used together with `HTTP` or `HTTPS` health monitor type.
    """

    max_retries_down: int
    """Number of failures before the member is switched to ERROR state."""

    url_path: Optional[str]
    """URL Path.

    Defaults to '/'. Can only be used together with `HTTP` or `HTTPS` health monitor
    type.
    """
