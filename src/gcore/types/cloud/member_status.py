# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["MemberStatus"]


class MemberStatus(BaseModel):
    id: str
    """UUID of the entity"""

    address: str
    """Address of the member (server)"""

    operating_status: LoadBalancerOperatingStatus
    """Operating status of the entity"""

    protocol_port: int
    """Port of the member (server)"""

    provisioning_status: ProvisioningStatus
    """Provisioning status of the entity"""
