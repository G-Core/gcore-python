# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel

__all__ = ["FileShare"]


class FileShare(BaseModel):
    id: str
    """File share ID"""

    connection_point: Optional[str] = None
    """Connection point. Can be null during File share creation"""

    created_at: str
    """Datetime when the file share was created"""

    creator_task_id: str
    """Task that created this entity"""

    name: str
    """File share name"""

    network_id: str
    """Network ID."""

    network_name: str
    """Network name."""

    project_id: int
    """Project ID"""

    protocol: str
    """File share protocol"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    share_network_name: Optional[str] = None
    """Share network name.

    May be null if the file share was created with volume type VAST
    """

    size: int
    """File share size, GiB"""

    status: Literal[
        "available",
        "awaiting_transfer",
        "backup_creating",
        "backup_restoring",
        "backup_restoring_error",
        "creating",
        "creating_from_snapshot",
        "deleted",
        "deleting",
        "ensuring",
        "error",
        "error_deleting",
        "extending",
        "extending_error",
        "inactive",
        "manage_error",
        "manage_starting",
        "migrating",
        "migrating_to",
        "replication_change",
        "reverting",
        "reverting_error",
        "shrinking",
        "shrinking_error",
        "shrinking_possible_data_loss_error",
        "unmanage_error",
        "unmanage_starting",
        "unmanaged",
    ]
    """File share status"""

    subnet_id: str
    """Subnet ID."""

    subnet_name: str
    """Subnet name."""

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

    type_name: Literal["standard", "vast"]
    """File share type name"""

    volume_type: Literal["default_share_type", "vast_share_type"]
    """File share disk type"""
