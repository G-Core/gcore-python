# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .tag import Tag
from ..._models import BaseModel
from .listener_status import ListenerStatus
from .provisioning_status import ProvisioningStatus
from .load_balancer_operating_status import LoadBalancerOperatingStatus

__all__ = ["LoadBalancerStatus"]


class LoadBalancerStatus(BaseModel):
    id: str
    """
    '#/components/schemas/LoadBalancerStatusSerializer/properties/id'
    "$.components.schemas.LoadBalancerStatusSerializer.properties.id"
    """

    listeners: List[ListenerStatus]
    """
    '#/components/schemas/LoadBalancerStatusSerializer/properties/listeners'
    "$.components.schemas.LoadBalancerStatusSerializer.properties.listeners"
    """

    name: str
    """
    '#/components/schemas/LoadBalancerStatusSerializer/properties/name'
    "$.components.schemas.LoadBalancerStatusSerializer.properties.name"
    """

    operating_status: LoadBalancerOperatingStatus
    """
    '#/components/schemas/LoadBalancerStatusSerializer/properties/operating_status'
    "$.components.schemas.LoadBalancerStatusSerializer.properties.operating_status"
    """

    provisioning_status: ProvisioningStatus
    """
    '#/components/schemas/LoadBalancerStatusSerializer/properties/provisioning_status'
    "$.components.schemas.LoadBalancerStatusSerializer.properties.provisioning_status"
    """

    metadata: Optional[List[Tag]] = None
    """
    '#/components/schemas/LoadBalancerStatusSerializer/properties/metadata'
    "$.components.schemas.LoadBalancerStatusSerializer.properties.metadata"
    """

    tags: Optional[List[Tag]] = None
    """
    '#/components/schemas/LoadBalancerStatusSerializer/properties/tags'
    "$.components.schemas.LoadBalancerStatusSerializer.properties.tags"
    """
