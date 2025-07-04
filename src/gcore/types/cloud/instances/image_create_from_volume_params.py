# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageCreateFromVolumeParams"]


class ImageCreateFromVolumeParams(TypedDict, total=False):
    project_id: int

    region_id: int

    name: Required[str]
    """Image name"""

    volume_id: Required[str]
    """Required if source is volume. Volume id"""

    architecture: Literal["aarch64", "x86_64"]
    """Image CPU architecture type: `aarch64`, `x86_64`"""

    hw_firmware_type: Optional[Literal["bios", "uefi"]]
    """Specifies the type of firmware with which to boot the guest."""

    hw_machine_type: Optional[Literal["pc", "q35"]]
    """A virtual chipset type."""

    is_baremetal: bool
    """Set to true if the image will be used by bare metal servers. Defaults to false."""

    os_type: Literal["linux", "windows"]
    """The operating system installed on the image."""

    source: Literal["volume"]
    """Image source"""

    ssh_key: Literal["allow", "deny", "required"]
    """Whether the image supports SSH key or not"""

    tags: Dict[str, str]
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """
