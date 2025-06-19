# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .tag_update_map_param import TagUpdateMapParam

__all__ = ["NetworkUpdateParams"]


class NetworkUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: str
    """Name."""

    tags: Optional[TagUpdateMapParam]
    """Update key-value tags using JSON Merge Patch semantics (RFC 7386).

    Provide key-value pairs to add or update tags. Set tag values to `null` to
    remove tags. Unspecified tags remain unchanged. Read-only tags are always
    preserved and cannot be modified. **Examples:**

    - **Add/update tags:**
      `{'tags': {'environment': 'production', 'team': 'backend'}}` adds new tags or
      updates existing ones.
    - **Delete tags:** `{'tags': {'`old_tag`': null}}` removes specific tags.
    - **Remove all tags:** `{'tags': null}` removes all user-managed tags (read-only
      tags are preserved).
    - **Partial update:** `{'tags': {'environment': 'staging'}}` only updates
      specified tags.
    - **Mixed operations:**
      `{'tags': {'environment': 'production', '`cost_center`': 'engineering', '`deprecated_tag`': null}}`
      adds/updates 'environment' and '`cost_center`' while removing
      '`deprecated_tag`', preserving other existing tags.
    - **Replace all:** first delete existing tags with null values, then add new
      ones in the same request.
    """
