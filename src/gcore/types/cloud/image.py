# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .tag import Tag
from ..._models import BaseModel

__all__ = ["Image"]


class Image(BaseModel):
    id: str
    """Image ID"""

    created_at: datetime
    """Datetime when the image was created"""

    disk_format: str
    """Disk format"""

    min_disk: int
    """Minimal boot volume required"""

    min_ram: int
    """Minimal VM RAM required"""

    name: str
    """Image display name"""

    os_distro: str
    """OS Distribution, i.e. Debian, CentOS, Ubuntu, CoreOS etc."""

    os_type: Literal["linux", "windows"]
    """The operating system installed on the image."""

    os_version: str
    """OS version, i.e. 19.04 (for Ubuntu) or 9.4 for Debian"""

    project_id: int
    """Project ID"""

    region: str
    """Region name"""

    region_id: int
    """Region ID"""

    size: int
    """Image size in bytes"""

    status: str
    """Image status, i.e. active"""

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

    architecture: Optional[Literal["aarch64", "x86_64"]] = None
    """An image architecture type: aarch64, `x86_64`"""

    creator_task_id: Optional[str] = None
    """Task that created this entity"""

    description: Optional[str] = None
    """Image description"""

    display_order: Optional[int] = None

    hw_firmware_type: Optional[Literal["bios", "uefi"]] = None
    """Specifies the type of firmware with which to boot the guest."""

    hw_machine_type: Optional[Literal["pc", "q35"]] = None
    """A virtual chipset type."""

    is_baremetal: Optional[bool] = None
    """Set to true if the image will be used by bare metal servers. Defaults to false."""

    ssh_key: Optional[Literal["allow", "deny", "required"]] = None
    """Whether the image supports SSH key or not"""

    task_id: Optional[str] = None
    """The UUID of the active task that currently holds a lock on the resource.

    This lock prevents concurrent modifications to ensure consistency. If `null`,
    the resource is not locked.
    """
