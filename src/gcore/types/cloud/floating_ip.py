# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel
from .floating_ip_status import FloatingIPStatus

__all__ = ["FloatingIP"]


class FloatingIP(BaseModel):
    id: str
    """Floating IP ID"""

    created_at: datetime
    """Datetime when the floating IP was created"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    fixed_ip_address: Optional[str] = None
    """IP address of the port the floating IP is attached to"""

    floating_ip_address: Optional[str] = None
    """IP Address of the floating IP"""

    port_id: Optional[str] = None
    """Port ID the floating IP is attached to.

    The `fixed_ip_address` is the IP address of the port.
    """

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    router_id: Optional[str] = None
    """Router ID"""

    status: Optional[FloatingIPStatus] = None
    """Floating IP status.

    DOWN - unassigned (available). ACTIVE - attached to a port (in use). ERROR -
    error state.
    """

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

    updated_at: datetime
    """Datetime when the floating IP was last updated"""
