# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .provisioning_status import ProvisioningStatus
from .lb_listener_protocol import LbListenerProtocol
from .load_balancer_statistics import LoadBalancerStatistics
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["LbListener", "UserList"]


class UserList(BaseModel):
    encrypted_password: str
    """
    '#/components/schemas/UserListItem/properties/encrypted_password'
    "$.components.schemas.UserListItem.properties.encrypted_password"
    """

    username: str
    """
    '#/components/schemas/UserListItem/properties/username'
    "$.components.schemas.UserListItem.properties.username"
    """


class LbListener(BaseModel):
    id: str
    """
    '#/components/schemas/LbListenerSerializer/properties/id'
    "$.components.schemas.LbListenerSerializer.properties.id"
    """

    connection_limit: int
    """
    '#/components/schemas/LbListenerSerializer/properties/connection_limit'
    "$.components.schemas.LbListenerSerializer.properties.connection_limit"
    """

    insert_headers: object
    """
    '#/components/schemas/LbListenerSerializer/properties/insert_headers'
    "$.components.schemas.LbListenerSerializer.properties.insert_headers"
    """

    name: str
    """
    '#/components/schemas/LbListenerSerializer/properties/name'
    "$.components.schemas.LbListenerSerializer.properties.name"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/LbListenerSerializer/properties/operating_status'
    "$.components.schemas.LbListenerSerializer.properties.operating_status"
    """

    protocol: LbListenerProtocol
    """
    '#/components/schemas/LbListenerSerializer/properties/protocol'
    "$.components.schemas.LbListenerSerializer.properties.protocol"
    """

    protocol_port: int
    """
    '#/components/schemas/LbListenerSerializer/properties/protocol_port'
    "$.components.schemas.LbListenerSerializer.properties.protocol_port"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/LbListenerSerializer/properties/provisioning_status'
    "$.components.schemas.LbListenerSerializer.properties.provisioning_status"
    """

    allowed_cidrs: Optional[List[str]] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/allowed_cidrs/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.allowed_cidrs.anyOf[0]"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.creator_task_id.anyOf[0]"
    """

    loadbalancer_id: Optional[str] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/loadbalancer_id/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.loadbalancer_id.anyOf[0]"
    """

    pool_count: Optional[int] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/pool_count/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.pool_count.anyOf[0]"
    """

    secret_id: Optional[str] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/secret_id/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.secret_id.anyOf[0]"
    """

    sni_secret_id: Optional[List[str]] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/sni_secret_id/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.sni_secret_id.anyOf[0]"
    """

    stats: Optional[LoadBalancerStatistics] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/stats/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.stats.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.task_id.anyOf[0]"
    """

    timeout_client_data: Optional[int] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/timeout_client_data/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.timeout_client_data.anyOf[0]"
    """

    timeout_member_connect: Optional[int] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/timeout_member_connect/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.timeout_member_connect.anyOf[0]"
    """

    timeout_member_data: Optional[int] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/timeout_member_data/anyOf/0'
    "$.components.schemas.LbListenerSerializer.properties.timeout_member_data.anyOf[0]"
    """

    user_list: Optional[List[UserList]] = None
    """
    '#/components/schemas/LbListenerSerializer/properties/user_list'
    "$.components.schemas.LbListenerSerializer.properties.user_list"
    """
