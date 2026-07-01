# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..tag_update_map_param import TagUpdateMapParam

__all__ = ["ClusterUpdateParams", "ServersSettings", "ServersSettingsCredentials"]


class ClusterUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    image_id: str
    """Image ID of the OS image to apply to the cluster template.

    Use GET /v1/images/{`project_id`}/{`region_id`} to discover available images.
    Takes effect on existing servers only after a successful POST /`apply_settings`
    call.
    """

    name: str
    """Cluster name"""

    servers_settings: ServersSettings
    """Configuration settings for the servers in the cluster"""

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


class ServersSettingsCredentials(TypedDict, total=False):
    """Optional server access credentials"""

    ssh_key_name: str
    """
    Specifies the name of the SSH keypair, created via the
    [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
    """


class ServersSettings(TypedDict, total=False):
    """Configuration settings for the servers in the cluster"""

    credentials: ServersSettingsCredentials
    """Optional server access credentials"""

    user_data: str
    """Optional custom user data (Base64-encoded)"""
