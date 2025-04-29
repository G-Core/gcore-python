# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["MemberStatus"]


class MemberStatus(BaseModel):
    id: str
    """
    '#/components/schemas/MemberStatusSerializer/properties/id'
    "$.components.schemas.MemberStatusSerializer.properties.id"
    """

    address: str
    """
    '#/components/schemas/MemberStatusSerializer/properties/address'
    "$.components.schemas.MemberStatusSerializer.properties.address"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/MemberStatusSerializer/properties/operating_status'
    "$.components.schemas.MemberStatusSerializer.properties.operating_status"
    """

    protocol_port: int
    """
    '#/components/schemas/MemberStatusSerializer/properties/protocol_port'
    "$.components.schemas.MemberStatusSerializer.properties.protocol_port"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/MemberStatusSerializer/properties/provisioning_status'
    "$.components.schemas.MemberStatusSerializer.properties.provisioning_status"
    """
