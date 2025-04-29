# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["DetailedLbPoolMember"]


class DetailedLbPoolMember(BaseModel):
    id: str
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/id'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.id"
    """

    address: str
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/address'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.address"
    """

    admin_state_up: bool
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/admin_state_up'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.admin_state_up"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/operating_status'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.operating_status"
    """

    protocol_port: int
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/protocol_port'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.protocol_port"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/provisioning_status'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.provisioning_status"
    """

    weight: int
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/weight'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.weight"
    """

    monitor_address: Optional[str] = None
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/monitor_address/anyOf/0'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.monitor_address.anyOf[0]"
    """

    monitor_port: Optional[int] = None
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/monitor_port/anyOf/0'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.monitor_port.anyOf[0]"
    """

    subnet_id: Optional[str] = None
    """
    '#/components/schemas/DetailedLbPoolMemberSerializer/properties/subnet_id/anyOf/0'
    "$.components.schemas.DetailedLbPoolMemberSerializer.properties.subnet_id.anyOf[0]"
    """
