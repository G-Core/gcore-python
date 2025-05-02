# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .tag import Tag
from ..._models import BaseModel

__all__ = ["GPUImage"]


class GPUImage(BaseModel):
    id: str
    """Image ID"""

    created_at: datetime
    """Datetime when the image was created"""

    min_disk: int
    """Minimal boot volume required"""

    min_ram: int
    """Minimal VM RAM required"""

    name: str
    """Image name"""

    status: str
    """Image status"""

    tags: List[Tag]
    """List of key-value tags associated with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """

    updated_at: datetime
    """Datetime when the image was updated"""

    visibility: str
    """Image visibility. Globally visible images are public"""

    architecture: Optional[str] = None
    """Image architecture type"""

    os_distro: Optional[str] = None
    """OS Distribution"""

    os_type: Optional[str] = None
    """The operating system installed on the image"""

    os_version: Optional[str] = None
    """OS version, i.e. 19.04 (for Ubuntu) or 9.4 for Debian"""

    size: Optional[int] = None
    """Image size in bytes."""

    ssh_key: Optional[str] = None
    """Whether the image supports SSH key or not"""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """
