# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel

__all__ = ["Snapshot"]


class Snapshot(BaseModel):
    id: str
    """Snapshot ID"""

    created_at: datetime
    """Datetime when the snapshot was created"""

    creator_task_id: str
    """Task that created this entity"""

    description: Optional[str] = None
    """Snapshot description"""

    name: str
    """Snapshot name"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    size: int
    """Snapshot size, GiB"""

    status: Literal[
        "available",
        "backing-up",
        "creating",
        "deleted",
        "deleting",
        "error",
        "error_deleting",
        "restoring",
        "unmanaging",
    ]
    """Snapshot status"""

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
    """Datetime when the snapshot was last updated"""

    volume_id: str
    """ID of the volume this snapshot was made from"""
