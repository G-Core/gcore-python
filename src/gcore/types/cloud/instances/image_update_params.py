# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..tag_update_map_param import TagUpdateMapParam

__all__ = ["ImageUpdateParams"]


class ImageUpdateParams(TypedDict, total=False):
    project_id: int

    region_id: int

    hw_firmware_type: Literal["bios", "uefi"]
    """Specifies the type of firmware with which to boot the guest."""

    hw_machine_type: Literal["pc", "q35"]
    """A virtual chipset type."""

    is_baremetal: bool
    """Set to true if the image will be used by bare metal servers."""

    name: str
    """Image display name"""

    os_type: Literal["linux", "windows"]
    """The operating system installed on the image."""

    ssh_key: Literal["allow", "deny", "required"]
    """Whether the image supports SSH key or not"""

    tags: TagUpdateMapParam
    """Key-value tags to associate with the resource.

    A tag is a key-value pair that can be associated with a resource, enabling
    efficient filtering and grouping for better organization and management. Some
    tags are read-only and cannot be modified by the user. Tags are also integrated
    with cost reports, allowing cost data to be filtered based on tag keys or
    values.
    """
