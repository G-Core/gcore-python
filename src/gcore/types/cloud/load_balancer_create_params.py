# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .http_method import HTTPMethod
from .lb_algorithm import LbAlgorithm
from .lb_pool_protocol import LbPoolProtocol
from .interface_ip_family import InterfaceIPFamily
from .lb_listener_protocol import LbListenerProtocol
from .lb_health_monitor_type import LbHealthMonitorType
from .lb_session_persistence_type import LbSessionPersistenceType
from .laas_index_retention_policy_param import LaasIndexRetentionPolicyParam
from .load_balancer_member_connectivity import LoadBalancerMemberConnectivity

__all__ = [
    "LoadBalancerCreateParams",
    "FloatingIP",
    "FloatingIPNewInstanceFloatingIPInterfaceSerializer",
    "FloatingIPExistingInstanceFloatingIPInterfaceSerializer",
    "Listener",
    "ListenerPool",
    "ListenerPoolHealthmonitor",
    "ListenerPoolMember",
    "ListenerPoolSessionPersistence",
    "ListenerUserList",
    "Logging",
]


class LoadBalancerCreateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    flavor: str
    """Load balancer flavor name"""

    floating_ip: FloatingIP
    """Floating IP configuration for assignment"""

    listeners: Iterable[Listener]
    """Load balancer listeners.

    Maximum 50 per LB (excluding Prometheus endpoint listener).
    """

    logging: Logging
    """Logging configuration"""

    name: str
    """Load balancer name"""

    name_template: str
    """Load balancer name which will be changed by template."""

    preferred_connectivity: LoadBalancerMemberConnectivity
    """
    Preferred option to establish connectivity between load balancer and its pools
    members. L2 provides best performance, L3 provides less IPs usage. It is taking
    effect only if `instance_id` + `ip_address` is provided, not `subnet_id` +
    `ip_address`, because we're considering this as intentional `subnet_id`
    specification.
    """

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    vip_ip_family: InterfaceIPFamily
    """
    IP family for load balancer subnet auto-selection if `vip_network_id` is
    specified
    """

    vip_network_id: str
    """Network ID for load balancer.

    If not specified, default external network will be used. Mutually exclusive with
    `vip_port_id`
    """

    vip_port_id: str
    """Existing Reserved Fixed IP port ID for load balancer.

    Mutually exclusive with `vip_network_id`
    """

    vip_subnet_id: str
    """Subnet ID for load balancer.

    If not specified, any subnet from `vip_network_id` will be selected. Ignored
    when `vip_network_id` is not specified.
    """


class FloatingIPNewInstanceFloatingIPInterfaceSerializer(TypedDict, total=False):
    source: Required[Literal["new"]]
    """A new floating IP will be created and attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


class FloatingIPExistingInstanceFloatingIPInterfaceSerializer(TypedDict, total=False):
    existing_floating_id: Required[str]
    """
    An existing available floating IP id must be specified if the source is set to
    `existing`
    """

    source: Required[Literal["existing"]]
    """An existing available floating IP will be attached to the instance.

    A floating IP is a public IP that makes the instance accessible from the
    internet, even if it only has a private IP. It works like SNAT, allowing
    outgoing and incoming traffic.
    """


FloatingIP: TypeAlias = Union[
    FloatingIPNewInstanceFloatingIPInterfaceSerializer, FloatingIPExistingInstanceFloatingIPInterfaceSerializer
]


class ListenerPoolHealthmonitor(TypedDict, total=False):
    delay: Required[int]
    """The time, in seconds, between sending probes to members"""

    max_retries: Required[int]
    """Number of successes before the member is switched to ONLINE state"""

    timeout: Required[int]
    """The maximum time to connect. Must be less than the delay value"""

    type: Required[LbHealthMonitorType]
    """Health monitor type. Once health monitor is created, cannot be changed."""

    expected_codes: Optional[str]
    """Can only be used together with `HTTP` or `HTTPS` health monitor type."""

    http_method: Optional[HTTPMethod]
    """HTTP method.

    Can only be used together with `HTTP` or `HTTPS` health monitor type.
    """

    max_retries_down: Optional[int]
    """Number of failures before the member is switched to ERROR state."""

    url_path: Optional[str]
    """URL Path.

    Defaults to '/'. Can only be used together with `HTTP` or `HTTPS` health monitor
    type.
    """


class ListenerPoolMember(TypedDict, total=False):
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


class ListenerPoolSessionPersistence(TypedDict, total=False):
    type: Required[LbSessionPersistenceType]
    """Session persistence type"""

    cookie_name: Optional[str]
    """Should be set if app cookie or http cookie is used"""

    persistence_granularity: Optional[str]
    """Subnet mask if `source_ip` is used. For UDP ports only"""

    persistence_timeout: Optional[int]
    """Session persistence timeout. For UDP ports only"""


class ListenerPool(TypedDict, total=False):
    lb_algorithm: Required[LbAlgorithm]
    """Load balancer algorithm"""

    name: Required[str]
    """Pool name"""

    protocol: Required[LbPoolProtocol]
    """Protocol"""

    ca_secret_id: Optional[str]
    """Secret ID of CA certificate bundle"""

    crl_secret_id: Optional[str]
    """Secret ID of CA revocation list file"""

    healthmonitor: Optional[ListenerPoolHealthmonitor]
    """Health monitor details"""

    listener_id: Optional[str]
    """Listener ID"""

    loadbalancer_id: Optional[str]
    """Loadbalancer ID"""

    members: Optional[Iterable[ListenerPoolMember]]
    """Pool members"""

    secret_id: Optional[str]
    """Secret ID for TLS client authentication to the member servers"""

    session_persistence: Optional[ListenerPoolSessionPersistence]
    """Session persistence details"""

    timeout_client_data: Optional[int]
    """Frontend client inactivity timeout in milliseconds"""

    timeout_member_connect: Optional[int]
    """Backend member connection timeout in milliseconds"""

    timeout_member_data: Optional[int]
    """Backend member inactivity timeout in milliseconds"""


class ListenerUserList(TypedDict, total=False):
    encrypted_password: Required[str]
    """Encrypted password to auth via Basic Authentication"""

    username: Required[str]
    """Username to auth via Basic Authentication"""


class Listener(TypedDict, total=False):
    name: Required[str]
    """Load balancer listener name"""

    protocol: Required[LbListenerProtocol]
    """Load balancer listener protocol"""

    protocol_port: Required[int]
    """Protocol port"""

    allowed_cidrs: Optional[List[str]]
    """Network CIDRs from which service will be accessible"""

    connection_limit: int
    """Limit of the simultaneous connections"""

    insert_x_forwarded: bool
    """Add headers X-Forwarded-For, X-Forwarded-Port, X-Forwarded-Proto to requests.

    Only used with HTTP or `TERMINATED_HTTPS` protocols.
    """

    pools: Iterable[ListenerPool]
    """Member pools"""

    secret_id: str
    """
    ID of the secret where PKCS12 file is stored for `TERMINATED_HTTPS` or
    PROMETHEUS listener
    """

    sni_secret_id: List[str]
    """
    List of secrets IDs containing PKCS12 format certificate/key bundles for
    `TERMINATED_HTTPS` or PROMETHEUS listeners
    """

    timeout_client_data: Optional[int]
    """Frontend client inactivity timeout in milliseconds"""

    timeout_member_connect: Optional[int]
    """Backend member connection timeout in milliseconds"""

    timeout_member_data: Optional[int]
    """Backend member inactivity timeout in milliseconds"""

    user_list: Iterable[ListenerUserList]
    """Load balancer listener list of username and encrypted password items"""


class Logging(TypedDict, total=False):
    destination_region_id: Optional[int]
    """Destination region id to which the logs will be written"""

    enabled: bool
    """Enable/disable forwarding logs to LaaS"""

    retention_policy: Optional[LaasIndexRetentionPolicyParam]
    """The logs retention policy"""

    topic_name: Optional[str]
    """The topic name to which the logs will be written"""
