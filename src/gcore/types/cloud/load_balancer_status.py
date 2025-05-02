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
    """UUID of the entity"""

    listeners: List[ListenerStatus]
    """Listeners of the Load Balancer"""

    name: str
    """Name of the load balancer"""

    operating_status: LoadBalancerOperatingStatus
    """Operating status of the entity"""

    provisioning_status: ProvisioningStatus
    """Provisioning status of the entity"""

    tags: Optional[List[Tag]] = None
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """
