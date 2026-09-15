# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo
from ...http_method import HTTPMethod

__all__ = ["HealthMonitorUpdateParams"]


class HealthMonitorUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    admin_state_up: bool
    """Administrative state of the resource.

    Omit to leave unchanged; `false` disables the resource so it will not process
    traffic.
    """

    delay: int
    """The time, in seconds, between sending probes to members.

    Omit to leave unchanged.
    """

    domain_name: Optional[str]
    """Domain name for HTTP host header.

    Can only be used together with `HTTP` or `HTTPS` health monitor type. Omit to
    leave unchanged. Set to `null` to clear the current value.
    """

    expected_codes: Optional[str]
    """Expected HTTP response codes.

    Can be a single code, a comma-separated list of codes, or a single range of
    codes. Can only be used together with `HTTP` or `HTTPS` health monitor type. For
    example, 200, 200,202,401,403,404, or 200-204. Omit to leave unchanged. Set to
    `null` to clear the current value.
    """

    http_method: Optional[HTTPMethod]
    """HTTP method.

    Can only be used together with `HTTP` or `HTTPS` health monitor type. Omit to
    leave unchanged. Set to `null` to clear the current value.
    """

    http_version: Optional[Literal["1.0", "1.1"]]
    """HTTP version.

    Can only be used together with `HTTP` or `HTTPS` health monitor type. Supported
    values: 1.0, 1.1. Omit to leave unchanged. Set to `null` to clear the current
    value.
    """

    max_retries: int
    """Number of successes before the member is switched to ONLINE state.

    Omit to leave unchanged.
    """

    max_retries_down: int
    """Number of failures before the member is switched to ERROR state.

    Omit to leave unchanged.
    """

    api_timeout: Annotated[int, PropertyInfo(alias="timeout")]
    """The maximum time to connect.

    Must be less than the delay value. Omit to leave unchanged.
    """

    url_path: Optional[str]
    """The HTTP path the health monitor requests on each member.

    Can only be used with `HTTP` or `HTTPS` health monitor type.

    Must start with `/` and contain only plain path segments. Query strings (`?`),
    fragments (`#`), percent-encoding (`%`), and consecutive slashes (`//`) are not
    allowed.

    Examples of valid paths:

    - `/` — check the root (most common)
    - `/healthz` — a dedicated health endpoint

    Omit to leave unchanged. Set to `null` to clear the current value.
    """
