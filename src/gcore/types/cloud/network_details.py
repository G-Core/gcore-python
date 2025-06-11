# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from .subnet import Subnet
from ..._models import BaseModel

__all__ = ["NetworkDetails"]


class NetworkDetails(BaseModel):
    id: str
    """Network ID"""

    created_at: datetime
    """Datetime when the network was created"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    default: Optional[bool] = None
    """True if network has `is_default` attribute"""

    external: bool
    """True if the network `router:external` attribute"""

    mtu: int
    """MTU (maximum transmission unit). Default value is 1450"""

    name: str
    """Network name"""

    port_security_enabled: bool
    """
    Indicates `port_security_enabled` status of all newly created in the network
    ports.
    """

    project_id: Optional[int] = None
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    segmentation_id: Optional[int] = None
    """Id of network segment"""

    shared: bool
    """True when the network is shared with your project by external owner"""

    subnets: List[Subnet]
    """List of subnets associated with the network"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """

    type: str
    """Network type (vlan, vxlan)"""

    updated_at: datetime
    """Datetime when the network was last updated"""
