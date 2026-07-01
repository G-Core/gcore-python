# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...tag import Tag
from ....._models import BaseModel

__all__ = ["GPUBaremetalClusterServer", "AppliedServersSettings", "SecurityGroup"]


class AppliedServersSettings(BaseModel):
    """
    Snapshot of cluster spec (`image_id` and `servers_settings`) applied when this server was last created or rebuilt. Compare with the cluster current spec to see what changed.
    """

    image_id: str

    servers_settings: Dict[str, object]


class SecurityGroup(BaseModel):
    id: str
    """Security group ID"""

    name: str
    """Security group name"""


class GPUBaremetalClusterServer(BaseModel):
    id: str
    """Server unique identifier"""

    applied_servers_settings: AppliedServersSettings
    """
    Snapshot of cluster spec (`image_id` and `servers_settings`) applied when this
    server was last created or rebuilt. Compare with the cluster current spec to see
    what changed.
    """

    created_at: datetime
    """Server creation date and time"""

    flavor: str
    """Unique flavor identifier"""

    has_pending_changes: bool
    """True if there are pending (not yet applied) server settings changes"""

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
