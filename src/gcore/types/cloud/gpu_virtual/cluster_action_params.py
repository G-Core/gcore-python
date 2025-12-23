# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..tag_update_map_param import TagUpdateMapParam

__all__ = [
    "ClusterActionParams",
    "StartVirtualGPUClusterSerializer",
    "StopVirtualGPUClusterSerializer",
    "SoftRebootVirtualGPUClusterSerializer",
    "HardRebootVirtualGPUClusterSerializer",
    "UpdateTagsGPUClusterSerializer",
    "ResizeVirtualGPUClusterSerializer",
]


class StartVirtualGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["start"]]
    """Action name"""


class StopVirtualGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["stop"]]
    """Action name"""


class SoftRebootVirtualGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["soft_reboot"]]
    """Action name"""


class HardRebootVirtualGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["hard_reboot"]]
    """Action name"""


class UpdateTagsGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["update_tags"]]
    """Action name"""

    tags: Required[Optional[TagUpdateMapParam]]
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
      adds/updates 'environment' and '`cost_center`' while removing
      '`deprecated_tag`', preserving other existing tags.

    - **Replace all:** first delete existing tags with null values, then add new
      ones in the same request.
    """


class ResizeVirtualGPUClusterSerializer(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    action: Required[Literal["resize"]]
    """Action name"""

    servers_count: Required[int]
    """Requested servers count"""


ClusterActionParams: TypeAlias = Union[
    StartVirtualGPUClusterSerializer,
    StopVirtualGPUClusterSerializer,
    SoftRebootVirtualGPUClusterSerializer,
    HardRebootVirtualGPUClusterSerializer,
    UpdateTagsGPUClusterSerializer,
    ResizeVirtualGPUClusterSerializer,
]
