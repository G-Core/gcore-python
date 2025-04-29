# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .lb_algorithm import LbAlgorithm
from .lb_pool_protocol import LbPoolProtocol
from .lb_health_monitor import LbHealthMonitor
from .provisioning_status import ProvisioningStatus
from .lb_session_persistence import LbSessionPersistence
from .detailed_lb_pool_member import DetailedLbPoolMember
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["DetailedLbPool", "Listener", "Loadbalancer"]


class Listener(BaseModel):
    id: str
    """
    '#/components/schemas/MandatoryIdSerializerPydantic/properties/id'
    "$.components.schemas.MandatoryIdSerializerPydantic.properties.id"
    """


class Loadbalancer(BaseModel):
    id: str
    """
    '#/components/schemas/MandatoryIdSerializerPydantic/properties/id'
    "$.components.schemas.MandatoryIdSerializerPydantic.properties.id"
    """


class DetailedLbPool(BaseModel):
    id: str
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/id'
    "$.components.schemas.DetailedLbPoolSerializer.properties.id"
    """

    ca_secret_id: Optional[str] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/ca_secret_id/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.ca_secret_id.anyOf[0]"
    """

    crl_secret_id: Optional[str] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/crl_secret_id/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.crl_secret_id.anyOf[0]"
    """

    lb_algorithm: LbAlgorithm
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/lb_algorithm'
    "$.components.schemas.DetailedLbPoolSerializer.properties.lb_algorithm"
    """

    listeners: List[Listener]
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/listeners'
    "$.components.schemas.DetailedLbPoolSerializer.properties.listeners"
    """

    loadbalancers: List[Loadbalancer]
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/loadbalancers'
    "$.components.schemas.DetailedLbPoolSerializer.properties.loadbalancers"
    """

    members: List[DetailedLbPoolMember]
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/members'
    "$.components.schemas.DetailedLbPoolSerializer.properties.members"
    """

    name: str
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/name'
    "$.components.schemas.DetailedLbPoolSerializer.properties.name"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/operating_status'
    "$.components.schemas.DetailedLbPoolSerializer.properties.operating_status"
    """

    protocol: LbPoolProtocol
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/protocol'
    "$.components.schemas.DetailedLbPoolSerializer.properties.protocol"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/provisioning_status'
    "$.components.schemas.DetailedLbPoolSerializer.properties.provisioning_status"
    """

    secret_id: Optional[str] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/secret_id/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.secret_id.anyOf[0]"
    """

    session_persistence: Optional[LbSessionPersistence] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/session_persistence/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.session_persistence.anyOf[0]"
    """

    timeout_client_data: Optional[int] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/timeout_client_data/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.timeout_client_data.anyOf[0]"
    """

    timeout_member_connect: Optional[int] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/timeout_member_connect/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.timeout_member_connect.anyOf[0]"
    """

    timeout_member_data: Optional[int] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/timeout_member_data/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.timeout_member_data.anyOf[0]"
    """

    creator_task_id: Optional[str] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/creator_task_id/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.creator_task_id.anyOf[0]"
    """

    healthmonitor: Optional[LbHealthMonitor] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/healthmonitor/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.healthmonitor.anyOf[0]"
    """

    task_id: Optional[str] = None
    """
    '#/components/schemas/DetailedLbPoolSerializer/properties/task_id/anyOf/0'
    "$.components.schemas.DetailedLbPoolSerializer.properties.task_id.anyOf[0]"
    """
