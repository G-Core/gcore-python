# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...tag import Tag
from ....._models import BaseModel

__all__ = ["GPUBaremetalClusterServer", "SecurityGroup"]


class SecurityGroup(BaseModel):
    id: str
    """Security group ID"""

    name: str
    """Security group name"""


class GPUBaremetalClusterServer(BaseModel):
    id: str
    """Server unique identifier"""

    created_at: datetime
    """Server creation date and time"""

    flavor: str
    """Unique flavor identifier"""

    image_id: Optional[str] = None
    """Server's image UUID"""

    ip_addresses: List[str]
    """List of IP addresses"""

    name: str
    """Server's name generated using cluster's name"""

    security_groups: List[SecurityGroup]
    """Security groups"""

    ssh_key_name: Optional[str] = None
    """SSH key pair assigned to the server"""

    status: Literal[
        "ACTIVE",
        "BUILD",
        "DELETED",
        "ERROR",
        "HARD_REBOOT",
        "MIGRATING",
        "PASSWORD",
        "PAUSED",
        "REBOOT",
        "REBUILD",
        "RESCUE",
        "RESIZE",
        "REVERT_RESIZE",
        "SHELVED",
        "SHELVED_OFFLOADED",
        "SHUTOFF",
        "SOFT_DELETED",
        "SUSPENDED",
        "UNKNOWN",
        "VERIFY_RESIZE",
    ]
    """Current server status"""

    tags: List[Tag]
    """User defined tags"""

    task_id: Optional[str] = None
    """Identifier of the task currently modifying the GPU cluster"""

    updated_at: datetime
    """Server update date and time"""
