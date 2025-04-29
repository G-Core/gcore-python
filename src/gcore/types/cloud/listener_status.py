# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .pool_status import PoolStatus
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["ListenerStatus"]


class ListenerStatus(BaseModel):
    id: str
    """
    '#/components/schemas/ListenerStatusSerializer/properties/id'
    "$.components.schemas.ListenerStatusSerializer.properties.id"
    """

    name: str
    """
    '#/components/schemas/ListenerStatusSerializer/properties/name'
    "$.components.schemas.ListenerStatusSerializer.properties.name"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/ListenerStatusSerializer/properties/operating_status'
    "$.components.schemas.ListenerStatusSerializer.properties.operating_status"
    """

    pools: List[PoolStatus]
    """
    '#/components/schemas/ListenerStatusSerializer/properties/pools'
    "$.components.schemas.ListenerStatusSerializer.properties.pools"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/ListenerStatusSerializer/properties/provisioning_status'
    "$.components.schemas.ListenerStatusSerializer.properties.provisioning_status"
    """
