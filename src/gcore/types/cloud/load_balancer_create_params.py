# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .http_method import HTTPMethod
from .lb_algorithm import LbAlgorithm
from .lb_pool_protocol import LbPoolProtocol
from .health_monitor_type import HealthMonitorType
from .interface_ip_family import InterfaceIPFamily
from .lb_listener_protocol import LbListenerProtocol
from .session_persistence_type import SessionPersistenceType
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
    "LoggingRetentionPolicy",
]


class LoadBalancerCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Floadbalancers%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/loadbalancers/{project_id}/{region_id}'].post.parameters[1].schema"
    """

    flavor: str
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/flavor'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.flavor"
    """

    floating_ip: FloatingIP
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/floating_ip'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.floating_ip"
    """

    listeners: Iterable[Listener]
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/listeners'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.listeners"
    """

    logging: Logging
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/logging'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.logging"
    """

    metadata: Dict[str, str]
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/metadata'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.metadata"
    """

    name: str
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/name'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.name"
    """

    name_template: str
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/name_template'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.name_template"
    """

    preferred_connectivity: LoadBalancerMemberConnectivity
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/preferred_connectivity'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.preferred_connectivity"
    """

    tag: List[str]
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/tag'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.tag"
    """

    vip_ip_family: InterfaceIPFamily
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_ip_family'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_ip_family"
    """

    vip_network_id: str
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_network_id'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_network_id"
    """

    vip_port_id: str
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_port_id'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_port_id"
    """

    vip_subnet_id: str
    """
    '#/components/schemas/CreateLoadbalancerSerializer/properties/vip_subnet_id'
    "$.components.schemas.CreateLoadbalancerSerializer.properties.vip_subnet_id"
    """


class FloatingIPNewInstanceFloatingIPInterfaceSerializer(TypedDict, total=False):
    source: Required[Literal["new"]]
    """
    '#/components/schemas/NewInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.NewInstanceFloatingIpInterfaceSerializer.properties.source"
    """


class FloatingIPExistingInstanceFloatingIPInterfaceSerializer(TypedDict, total=False):
    existing_floating_id: Required[str]
    """
    '#/components/schemas/ExistingInstanceFloatingIpInterfaceSerializer/properties/existing_floating_id'
    "$.components.schemas.ExistingInstanceFloatingIpInterfaceSerializer.properties.existing_floating_id"
    """

    source: Required[Literal["existing"]]
    """
    '#/components/schemas/ExistingInstanceFloatingIpInterfaceSerializer/properties/source'
    "$.components.schemas.ExistingInstanceFloatingIpInterfaceSerializer.properties.source"
    """


FloatingIP: TypeAlias = Union[
    FloatingIPNewInstanceFloatingIPInterfaceSerializer, FloatingIPExistingInstanceFloatingIPInterfaceSerializer
]


class ListenerPoolHealthmonitor(TypedDict, total=False):
    delay: Required[int]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/delay'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.delay"
    """

    max_retries: Required[int]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/max_retries'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.max_retries"
    """

    timeout: Required[int]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/timeout'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.timeout"
    """

    type: Required[HealthMonitorType]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/type'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.type"
    """

    expected_codes: Optional[str]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/expected_codes/anyOf/0'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.expected_codes.anyOf[0]"
    """

    http_method: Optional[HTTPMethod]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/http_method/anyOf/0'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.http_method.anyOf[0]"
    """

    max_retries_down: Optional[int]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/max_retries_down/anyOf/0'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.max_retries_down.anyOf[0]"
    """

    url_path: Optional[str]
    """
    '#/components/schemas/CreateLbHealthMonitorSerializer/properties/url_path/anyOf/0'
    "$.components.schemas.CreateLbHealthMonitorSerializer.properties.url_path.anyOf[0]"
    """


class ListenerPoolMember(TypedDict, total=False):
    address: Required[str]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/address'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.address"
    """

    protocol_port: Required[int]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/protocol_port'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.protocol_port"
    """

    admin_state_up: Optional[bool]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/admin_state_up/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.admin_state_up.anyOf[0]"
    """

    instance_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/instance_id/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.instance_id.anyOf[0]"
    """

    monitor_address: Optional[str]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/monitor_address/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.monitor_address.anyOf[0]"
    """

    monitor_port: Optional[int]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/monitor_port/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.monitor_port.anyOf[0]"
    """

    subnet_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/subnet_id/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.subnet_id.anyOf[0]"
    """

    weight: Optional[int]
    """
    '#/components/schemas/CreateLbPoolMemberSerializer/properties/weight/anyOf/0'
    "$.components.schemas.CreateLbPoolMemberSerializer.properties.weight.anyOf[0]"
    """


class ListenerPoolSessionPersistence(TypedDict, total=False):
    type: Required[SessionPersistenceType]
    """
    '#/components/schemas/MutateLbSessionPersistence/properties/type'
    "$.components.schemas.MutateLbSessionPersistence.properties.type"
    """

    cookie_name: Optional[str]
    """
    '#/components/schemas/MutateLbSessionPersistence/properties/cookie_name/anyOf/0'
    "$.components.schemas.MutateLbSessionPersistence.properties.cookie_name.anyOf[0]"
    """

    persistence_granularity: Optional[str]
    """
    '#/components/schemas/MutateLbSessionPersistence/properties/persistence_granularity/anyOf/0'
    "$.components.schemas.MutateLbSessionPersistence.properties.persistence_granularity.anyOf[0]"
    """

    persistence_timeout: Optional[int]
    """
    '#/components/schemas/MutateLbSessionPersistence/properties/persistence_timeout/anyOf/0'
    "$.components.schemas.MutateLbSessionPersistence.properties.persistence_timeout.anyOf[0]"
    """


class ListenerPool(TypedDict, total=False):
    lb_algorithm: Required[LbAlgorithm]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/lb_algorithm'
    "$.components.schemas.CreateLbPoolSerializer.properties.lb_algorithm"
    """

    name: Required[str]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/name'
    "$.components.schemas.CreateLbPoolSerializer.properties.name"
    """

    protocol: Required[LbPoolProtocol]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/protocol'
    "$.components.schemas.CreateLbPoolSerializer.properties.protocol"
    """

    ca_secret_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/ca_secret_id/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.ca_secret_id.anyOf[0]"
    """

    crl_secret_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/crl_secret_id/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.crl_secret_id.anyOf[0]"
    """

    healthmonitor: Optional[ListenerPoolHealthmonitor]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/healthmonitor/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.healthmonitor.anyOf[0]"
    """

    listener_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/listener_id/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.listener_id.anyOf[0]"
    """

    loadbalancer_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/loadbalancer_id/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.loadbalancer_id.anyOf[0]"
    """

    members: Optional[Iterable[ListenerPoolMember]]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/members/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.members.anyOf[0]"
    """

    secret_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/secret_id/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.secret_id.anyOf[0]"
    """

    session_persistence: Optional[ListenerPoolSessionPersistence]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/session_persistence/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.session_persistence.anyOf[0]"
    """

    timeout_client_data: Optional[int]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/timeout_client_data/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.timeout_client_data.anyOf[0]"
    """

    timeout_member_connect: Optional[int]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/timeout_member_connect/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.timeout_member_connect.anyOf[0]"
    """

    timeout_member_data: Optional[int]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/timeout_member_data/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.timeout_member_data.anyOf[0]"
    """


class ListenerUserList(TypedDict, total=False):
    encrypted_password: Required[str]
    """
    '#/components/schemas/UserListItem/properties/encrypted_password'
    "$.components.schemas.UserListItem.properties.encrypted_password"
    """

    username: Required[str]
    """
    '#/components/schemas/UserListItem/properties/username'
    "$.components.schemas.UserListItem.properties.username"
    """


class Listener(TypedDict, total=False):
    name: Required[str]
    """
    '#/components/schemas/CreateListenerSerializer/properties/name'
    "$.components.schemas.CreateListenerSerializer.properties.name"
    """

    protocol: Required[LbListenerProtocol]
    """
    '#/components/schemas/CreateListenerSerializer/properties/protocol'
    "$.components.schemas.CreateListenerSerializer.properties.protocol"
    """

    protocol_port: Required[int]
    """
    '#/components/schemas/CreateListenerSerializer/properties/protocol_port'
    "$.components.schemas.CreateListenerSerializer.properties.protocol_port"
    """

    allowed_cidrs: Optional[List[str]]
    """
    '#/components/schemas/CreateListenerSerializer/properties/allowed_cidrs/anyOf/0'
    "$.components.schemas.CreateListenerSerializer.properties.allowed_cidrs.anyOf[0]"
    """

    connection_limit: int
    """
    '#/components/schemas/CreateListenerSerializer/properties/connection_limit'
    "$.components.schemas.CreateListenerSerializer.properties.connection_limit"
    """

    insert_x_forwarded: bool
    """
    '#/components/schemas/CreateListenerSerializer/properties/insert_x_forwarded'
    "$.components.schemas.CreateListenerSerializer.properties.insert_x_forwarded"
    """

    pools: Iterable[ListenerPool]
    """
    '#/components/schemas/CreateListenerSerializer/properties/pools'
    "$.components.schemas.CreateListenerSerializer.properties.pools"
    """

    secret_id: str
    """
    '#/components/schemas/CreateListenerSerializer/properties/secret_id/anyOf/0'
    "$.components.schemas.CreateListenerSerializer.properties.secret_id.anyOf[0]"
    """

    sni_secret_id: List[str]
    """
    '#/components/schemas/CreateListenerSerializer/properties/sni_secret_id'
    "$.components.schemas.CreateListenerSerializer.properties.sni_secret_id"
    """

    timeout_client_data: Optional[int]
    """
    '#/components/schemas/CreateListenerSerializer/properties/timeout_client_data/anyOf/0'
    "$.components.schemas.CreateListenerSerializer.properties.timeout_client_data.anyOf[0]"
    """

    timeout_member_connect: Optional[int]
    """
    '#/components/schemas/CreateListenerSerializer/properties/timeout_member_connect/anyOf/0'
    "$.components.schemas.CreateListenerSerializer.properties.timeout_member_connect.anyOf[0]"
    """

    timeout_member_data: Optional[int]
    """
    '#/components/schemas/CreateListenerSerializer/properties/timeout_member_data/anyOf/0'
    "$.components.schemas.CreateListenerSerializer.properties.timeout_member_data.anyOf[0]"
    """

    user_list: Iterable[ListenerUserList]
    """
    '#/components/schemas/CreateListenerSerializer/properties/user_list'
    "$.components.schemas.CreateListenerSerializer.properties.user_list"
    """


class LoggingRetentionPolicy(TypedDict, total=False):
    period: Required[Optional[int]]
    """
    '#/components/schemas/LaasIndexRetentionPolicyPydanticSerializer/properties/period/anyOf/0'
    "$.components.schemas.LaasIndexRetentionPolicyPydanticSerializer.properties.period.anyOf[0]"
    """


class Logging(TypedDict, total=False):
    destination_region_id: Optional[int]
    """
    '#/components/schemas/LoadbalancerLoggingSerializer/properties/destination_region_id/anyOf/0'
    "$.components.schemas.LoadbalancerLoggingSerializer.properties.destination_region_id.anyOf[0]"
    """

    enabled: bool
    """
    '#/components/schemas/LoadbalancerLoggingSerializer/properties/enabled'
    "$.components.schemas.LoadbalancerLoggingSerializer.properties.enabled"
    """

    retention_policy: Optional[LoggingRetentionPolicy]
    """
    '#/components/schemas/LoadbalancerLoggingSerializer/properties/retention_policy/anyOf/0'
    "$.components.schemas.LoadbalancerLoggingSerializer.properties.retention_policy.anyOf[0]"
    """

    topic_name: Optional[str]
    """
    '#/components/schemas/LoadbalancerLoggingSerializer/properties/topic_name/anyOf/0'
    "$.components.schemas.LoadbalancerLoggingSerializer.properties.topic_name.anyOf[0]"
    """
