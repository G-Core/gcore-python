# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..http_method import HTTPMethod
from ..lb_algorithm import LbAlgorithm
from ..lb_pool_protocol import LbPoolProtocol
from ..lb_health_monitor_type import LbHealthMonitorType
from ..lb_session_persistence_type import LbSessionPersistenceType

__all__ = ["PoolUpdateParams", "Healthmonitor", "Member", "SessionPersistence"]


class PoolUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    ca_secret_id: Optional[str]
    """Secret ID of CA certificate bundle"""

    crl_secret_id: Optional[str]
    """Secret ID of CA revocation list file"""

    healthmonitor: Optional[Healthmonitor]
    """New pool health monitor settings"""

    lb_algorithm: LbAlgorithm
    """New load balancer pool algorithm of how to distribute requests"""

    members: Optional[Iterable[Member]]
    """New sequence of load balancer pool members.

    If members are the same (by address + port), they will be kept as is without
    recreation and downtime.
    """

    name: str
    """New pool name"""

    protocol: LbPoolProtocol
    """New communication protocol"""

    secret_id: Optional[str]
    """Secret ID for TLS client authentication to the member servers"""

    session_persistence: Optional[SessionPersistence]
    """New session persistence settings"""

    timeout_client_data: Optional[int]
    """Frontend client inactivity timeout in milliseconds"""

    timeout_member_connect: Optional[int]
    """Backend member connection timeout in milliseconds"""

    timeout_member_data: Optional[int]
    """Backend member inactivity timeout in milliseconds"""


class Healthmonitor(TypedDict, total=False):
    delay: Required[int]
    """The time, in seconds, between sending probes to members"""

    max_retries: Required[int]
    """Number of successes before the member is switched to ONLINE state"""

    timeout: Required[int]
    """The maximum time to connect. Must be less than the delay value"""

    expected_codes: Optional[str]
    """Can only be used together with `HTTP` or `HTTPS` health monitor type."""

    http_method: Optional[HTTPMethod]
    """HTTP method.

    Can only be used together with `HTTP` or `HTTPS` health monitor type.
    """

    max_retries_down: Optional[int]
    """Number of failures before the member is switched to ERROR state."""

    type: Optional[LbHealthMonitorType]
    """Health monitor type. Once health monitor is created, cannot be changed."""

    url_path: Optional[str]
    """URL Path.

    Defaults to '/'. Can only be used together with `HTTP` or `HTTPS` health monitor
    type.
    """


class Member(TypedDict, total=False):
    address: Required[str]
    """Member IP address"""

    protocol_port: Required[int]
    """Member IP port"""

    admin_state_up: Optional[bool]
    """Administrative state of the resource.

    When set to true, the resource is enabled and operational. When set to false,
    the resource is disabled and will not process traffic. When null is passed, the
    value is skipped and defaults to true.
    """

    instance_id: Optional[str]
    """Either `subnet_id` or `instance_id` should be provided"""

    monitor_address: Optional[str]
    """An alternate IP address used for health monitoring of a backend member.

    Default is null which monitors the member address.
    """

    monitor_port: Optional[int]
    """An alternate protocol port used for health monitoring of a backend member.

    Default is null which monitors the member `protocol_port`.
    """

    subnet_id: Optional[str]
    """Either `subnet_id` or `instance_id` should be provided"""

    weight: Optional[int]
    """Member weight. Valid values: 0 to 256, defaults to 1"""


class SessionPersistence(TypedDict, total=False):
    type: Required[LbSessionPersistenceType]
    """Session persistence type"""

    cookie_name: Optional[str]
    """Should be set if app cookie or http cookie is used"""

    persistence_granularity: Optional[str]
    """Subnet mask if `source_ip` is used. For UDP ports only"""

    persistence_timeout: Optional[int]
    """Session persistence timeout. For UDP ports only"""
