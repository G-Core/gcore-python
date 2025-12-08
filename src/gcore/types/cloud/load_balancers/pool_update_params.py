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
    """New pool health monitor settings"""

    delay: Required[int]
    """The time, in seconds, between sending probes to members"""

    max_retries: Required[int]
    """Number of successes before the member is switched to ONLINE state"""

    timeout: Required[int]
    """The maximum time to connect. Must be less than the delay value"""

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

    admin_state_up: bool
    """Administrative state of the resource.

    When set to true, the resource is enabled and operational. When set to false,
    the resource is disabled and will not process traffic. When null is passed, the
    value is skipped and defaults to true.
    """

    backup: bool
    """
    Set to true if the member is a backup member, to which traffic will be sent
    exclusively when all non-backup members will be unreachable. It allows to
    realize ACTIVE-BACKUP load balancing without thinking about VRRP and VIP
    configuration. Default is false.
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
    """`subnet_id` in which `address` is present.

    Either `subnet_id` or `instance_id` should be provided
    """

    weight: int
    """Member weight.

    Valid values are 0 < `weight` <= 256, defaults to 1. Controls traffic
    distribution based on the pool's load balancing algorithm:

    - `ROUND_ROBIN`: Distributes connections to each member in turn according to
      weights. Higher weight = more turns in the cycle. Example: weights 3 vs 1 =
      ~75% vs ~25% of requests.
    - `LEAST_CONNECTIONS`: Sends new connections to the member with fewest active
      connections, performing round-robin within groups of the same normalized load.
      Higher weight = allowed to hold more simultaneous connections before being
      considered 'more loaded'. Example: weights 2 vs 1 means 20 vs 10 active
      connections is treated as balanced.
    - `SOURCE_IP`: Routes clients consistently to the same member by hashing client
      source IP; hash result is modulo total weight of running members. Higher
      weight = more hash buckets, so more client IPs map to that member. Example:
      weights 2 vs 1 = roughly two-thirds of distinct client IPs map to the
      higher-weight member.
    """


class SessionPersistence(TypedDict, total=False):
    """New session persistence settings"""

    type: Required[LbSessionPersistenceType]
    """Session persistence type"""

    cookie_name: Optional[str]
    """Should be set if app cookie or http cookie is used"""

    persistence_granularity: Optional[str]
    """Subnet mask if `source_ip` is used. For UDP ports only"""

    persistence_timeout: Optional[int]
    """Session persistence timeout. For UDP ports only"""
