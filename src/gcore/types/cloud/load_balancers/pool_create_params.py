# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..http_method import HTTPMethod
from ..lb_algorithm import LbAlgorithm
from ..lb_pool_protocol import LbPoolProtocol
from ..health_monitor_type import HealthMonitorType
from ..session_persistence_type import SessionPersistenceType

__all__ = ["PoolCreateParams", "Healthmonitor", "Member", "SessionPersistence"]


class PoolCreateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/0/schema'
    "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].post.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D/post/parameters/1/schema'
    "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}'].post.parameters[1].schema"
    """

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

    healthmonitor: Optional[Healthmonitor]
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

    members: Optional[Iterable[Member]]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/members/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.members.anyOf[0]"
    """

    secret_id: Optional[str]
    """
    '#/components/schemas/CreateLbPoolSerializer/properties/secret_id/anyOf/0'
    "$.components.schemas.CreateLbPoolSerializer.properties.secret_id.anyOf[0]"
    """

    session_persistence: Optional[SessionPersistence]
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


class Healthmonitor(TypedDict, total=False):
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


class Member(TypedDict, total=False):
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


class SessionPersistence(TypedDict, total=False):
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
