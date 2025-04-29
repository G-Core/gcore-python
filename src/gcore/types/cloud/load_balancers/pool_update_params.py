# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..http_method import HTTPMethod
from ..lb_algorithm import LbAlgorithm
from ..lb_pool_protocol import LbPoolProtocol
from ..health_monitor_type import HealthMonitorType
from ..session_persistence_type import SessionPersistenceType

__all__ = ["PoolUpdateParams", "Healthmonitor", "Member", "SessionPersistence"]


class PoolUpdateParams(TypedDict, total=False):
    project_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/patch/parameters/0/schema'
    "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].patch.parameters[0].schema"
    """

    region_id: int
    """
    '#/paths/%2Fcloud%2Fv1%2Flbpools%2F%7Bproject_id%7D%2F%7Bregion_id%7D%2F%7Bpool_id%7D/patch/parameters/1/schema'
    "$.paths['/cloud/v1/lbpools/{project_id}/{region_id}/{pool_id}'].patch.parameters[1].schema"
    """

    ca_secret_id: Optional[str]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/ca_secret_id/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.ca_secret_id.anyOf[0]"
    """

    crl_secret_id: Optional[str]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/crl_secret_id/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.crl_secret_id.anyOf[0]"
    """

    healthmonitor: Optional[Healthmonitor]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/healthmonitor/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.healthmonitor.anyOf[0]"
    """

    lb_algorithm: LbAlgorithm
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/lb_algorithm'
    "$.components.schemas.PatchLbPoolSerializer.properties.lb_algorithm"
    """

    members: Optional[Iterable[Member]]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/members/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.members.anyOf[0]"
    """

    name: str
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/name'
    "$.components.schemas.PatchLbPoolSerializer.properties.name"
    """

    protocol: LbPoolProtocol
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/protocol'
    "$.components.schemas.PatchLbPoolSerializer.properties.protocol"
    """

    secret_id: Optional[str]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/secret_id/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.secret_id.anyOf[0]"
    """

    session_persistence: Optional[SessionPersistence]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/session_persistence/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.session_persistence.anyOf[0]"
    """

    timeout_client_data: Optional[int]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/timeout_client_data/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.timeout_client_data.anyOf[0]"
    """

    timeout_member_connect: Optional[int]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/timeout_member_connect/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.timeout_member_connect.anyOf[0]"
    """

    timeout_member_data: Optional[int]
    """
    '#/components/schemas/PatchLbPoolSerializer/properties/timeout_member_data/anyOf/0'
    "$.components.schemas.PatchLbPoolSerializer.properties.timeout_member_data.anyOf[0]"
    """


class Healthmonitor(TypedDict, total=False):
    delay: Required[int]
    """
    '#/components/schemas/PatchLbHealthMonitorSerializer/properties/delay'
    "$.components.schemas.PatchLbHealthMonitorSerializer.properties.delay"
    """

    max_retries: Required[int]
    """
    '#/components/schemas/PatchLbHealthMonitorSerializer/properties/max_retries'
    "$.components.schemas.PatchLbHealthMonitorSerializer.properties.max_retries"
    """

    timeout: Required[int]
    """
    '#/components/schemas/PatchLbHealthMonitorSerializer/properties/timeout'
    "$.components.schemas.PatchLbHealthMonitorSerializer.properties.timeout"
    """

    expected_codes: Optional[str]
    """
    '#/components/schemas/PatchLbHealthMonitorSerializer/properties/expected_codes/anyOf/0'
    "$.components.schemas.PatchLbHealthMonitorSerializer.properties.expected_codes.anyOf[0]"
    """

    http_method: Optional[HTTPMethod]
    """
    '#/components/schemas/PatchLbHealthMonitorSerializer/properties/http_method/anyOf/0'
    "$.components.schemas.PatchLbHealthMonitorSerializer.properties.http_method.anyOf[0]"
    """

    max_retries_down: Optional[int]
    """
    '#/components/schemas/PatchLbHealthMonitorSerializer/properties/max_retries_down/anyOf/0'
    "$.components.schemas.PatchLbHealthMonitorSerializer.properties.max_retries_down.anyOf[0]"
    """

    type: Optional[HealthMonitorType]
    """
    '#/components/schemas/PatchLbHealthMonitorSerializer/properties/type/anyOf/0'
    "$.components.schemas.PatchLbHealthMonitorSerializer.properties.type.anyOf[0]"
    """

    url_path: Optional[str]
    """
    '#/components/schemas/PatchLbHealthMonitorSerializer/properties/url_path/anyOf/0'
    "$.components.schemas.PatchLbHealthMonitorSerializer.properties.url_path.anyOf[0]"
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
