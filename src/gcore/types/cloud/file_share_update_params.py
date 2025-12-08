# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .tag_update_map_param import TagUpdateMapParam

__all__ = ["FileShareUpdateParams", "ShareSettings"]


class FileShareUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    name: str
    """Name"""

    share_settings: ShareSettings
    """Configuration settings for the share"""

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
      adds/updates 'environment' and '`cost_center`' while removing
      '`deprecated_tag`', preserving other existing tags.

    - **Replace all:** first delete existing tags with null values, then add new
      ones in the same request.
    """


class ShareSettings(TypedDict, total=False):
    """Configuration settings for the share"""

    allowed_characters: Literal["LCD", "NPL"]
    """Determines which characters are allowed in file names. Choose between:

    - Lowest Common Denominator (LCD), allows only characters allowed by all VAST
      Cluster-supported protocols
    - Native Protocol Limit (NPL), imposes no limitation beyond that of the client
      protocol.
    """

    path_length: Literal["LCD", "NPL"]
    """Affects the maximum limit of file path component name length. Choose between:

    - Lowest Common Denominator (LCD), imposes the lowest common denominator file
      length limit of all VAST Cluster-supported protocols. With this (default)
      option, the limitation on the length of a single component of the path is 255
      characters
    - Native Protocol Limit (NPL), imposes no limitation beyond that of the client
      protocol.
    """

    root_squash: bool
    """Enables or disables root squash for NFS clients.

    - If `true` (default), root squash is enabled: the root user is mapped to nobody
      for all file and folder management operations on the export.
    - If `false`, root squash is disabled: the NFS client `root` user retains root
      privileges. Use this option if you trust the root user not to perform
      operations that will corrupt data.
    """
