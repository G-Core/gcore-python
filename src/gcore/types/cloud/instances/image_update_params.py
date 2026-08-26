# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..tag_update_map_param import TagUpdateMapParam

__all__ = ["ImageUpdateParams"]


class ImageUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    hw_firmware_type: Literal["bios", "uefi"]
    """Specifies the type of firmware with which to boot the guest."""

    hw_machine_type: Literal["i440", "q35"]
    """A virtual chipset type."""

    is_baremetal: Optional[bool]
    """Set to true if the image will be used by bare metal servers."""

    name: str
    """Image display name"""

    os_type: Literal["linux", "windows"]
    """The operating system installed on the image."""

    ssh_key: Literal["allow", "deny", "required"]
    """Whether the image supports SSH key or not"""

    tags: Optional[TagUpdateMapParam]
    """Update key-value tags using JSON Merge Patch semantics (RFC 7386).

    Provide key-value pairs to add or update tags. Set tag values to `null` to
    remove tags. Unspecified tags remain unchanged. Read-only tags are always
    preserved and cannot be modified.

    **Examples:**

    - **Add/update tags:**
      `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
      updates existing ones.
    - **Delete tags:** `{'tags': {'old_tag': null}}` removes specific tags.
    - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
      tags are preserved).
    - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
      specified tags.
    - **Mixed operations:**
      `{'tags': {'environment': 'production', 'cost_center': 'engineering', 'deprecated_tag': null}}`
      adds/updates 'environment' and 'cost_center' while removing 'deprecated_tag',
      preserving other existing tags.
    - **Replace all:** first delete existing tags with null values, then add new
      ones in the same request.
    """
