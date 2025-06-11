# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .load_balancer_l7_rule import LoadBalancerL7Rule

__all__ = ["LoadBalancerL7Policy"]


class LoadBalancerL7Policy(BaseModel):
    id: Optional[str] = None
    """ID"""

    action: Optional[Literal["REDIRECT_PREFIX", "REDIRECT_TO_POOL", "REDIRECT_TO_URL", "REJECT"]] = None
    """Action"""

    listener_id: Optional[str] = None
    """Listener ID"""

    name: Optional[str] = None
    """Human-readable name of the policy"""

    operating_status: Optional[Literal["DEGRADED", "DRAINING", "ERROR", "NO_MONITOR", "OFFLINE", "ONLINE"]] = None
    """L7 policy operating status"""

    position: Optional[int] = None
    """The position of this policy on the listener. Positions start at 1."""

    project_id: Optional[int] = None
    """Project ID"""

    provisioning_status: Optional[
        Literal["ACTIVE", "DELETED", "ERROR", "PENDING_CREATE", "PENDING_DELETE", "PENDING_UPDATE"]
    ] = None

    redirect_http_code: Optional[int] = None
    """
    Requests matching this policy will be redirected to the specified URL or Prefix
    URL with the HTTP response code. Valid if action is `REDIRECT_TO_URL` or
    `REDIRECT_PREFIX`. Valid options are 301, 302, 303, 307, or 308. Default is 302.
    """

    redirect_pool_id: Optional[str] = None
    """Requests matching this policy will be redirected to the pool with this ID.

    Only valid if action is `REDIRECT_TO_POOL`.
    """

    redirect_prefix: Optional[str] = None
    """Requests matching this policy will be redirected to this Prefix URL.

    Only valid if action is `REDIRECT_PREFIX`.
    """

    redirect_url: Optional[str] = None
    """Requests matching this policy will be redirected to this URL.

    Only valid if action is `REDIRECT_TO_URL`.
    """

    region: Optional[str] = None
    """Region name"""

    region_id: Optional[int] = None
    """Region ID"""

    rules: Optional[List[LoadBalancerL7Rule]] = None
    """Rules.

    All the rules associated with a given policy are logically ANDed together. A
    request must match all the policy’s rules to match the policy.If you need to
    express a logical OR operation between rules, then do this by creating multiple
    policies with the same action.
    """

    tags: Optional[List[str]] = None
    """A list of simple strings assigned to the resource."""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """
