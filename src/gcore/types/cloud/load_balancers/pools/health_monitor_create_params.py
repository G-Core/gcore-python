# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

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

    admin_state_up: bool
    """Administrative state of the resource.

    When set to true, the resource is enabled and operational. When set to false,
    the resource is disabled and will not process traffic. Defaults to true.
    """

    domain_name: Optional[str]
    """Domain name for HTTP host header.

    Can only be used together with `HTTP` or `HTTPS` health monitor type. A name has
    1 to 253 characters. A name has labels that a dot separates, and can end with a
    dot. A label has 1 to 63 characters. A label starts with a letter, a digit or an
    underscore. The other characters of a label are letters, digits or hyphens. A
    label does not end with a hyphen.
    """

    expected_codes: Optional[str]
    """Expected HTTP response codes.

    Can be a single code, a comma-separated list of codes, or a single range of
    codes. Can only be used together with `HTTP` or `HTTPS` health monitor type. A
    code has three digits from 100 to 599. The first code of a range is not greater
    than the last code. For example, 200, 200,202,401,403,404, or 200-204. A value
    has 1 to 64 characters. If not specified, the default is 200.
    """

    http_method: Optional[HTTPMethod]
    """HTTP method.

    Can only be used together with `HTTP` or `HTTPS` health monitor type.
    """

    http_version: Optional[Literal["1.0", "1.1"]]
    """HTTP version.

    Can only be used together with `HTTP` or `HTTPS` health monitor type. Supported
    values: 1.0, 1.1.
    """

    max_retries_down: int
    """Number of failures before the member is switched to ERROR state."""

    url_path: Optional[str]
    """The HTTP path the health monitor requests on each member.

    Defaults to `/` if not set. Can only be used with `HTTP` or `HTTPS` health
    monitor type.

    Must start with `/` and has 1 to 255 characters. The path cannot start with
    `//`. Query strings (`?`), fragments (`#`), spaces and control characters are
    not allowed.

    Examples of valid paths:

    - `/` — check the root (most common, default)
    - `/healthz` — a dedicated health endpoint
    """
