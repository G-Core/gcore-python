# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..tag_update_map_param import TagUpdateMapParam

__all__ = [
    "ClusterUpdateParams",
    "ServersSettings",
    "ServersSettingsCredentials",
    "ServersSettingsVolume",
    "ServersSettingsVolumeNewVolumeInputSerializer",
    "ServersSettingsVolumeImageVolumeInputSerializer",
]


class ClusterUpdateParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

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


class ServersSettingsVolumeNewVolumeInputSerializer(TypedDict, total=False):
    boot_index: Required[int]
    """Boot index of the volume"""

    name: Required[str]
    """Volume name"""

    size: Required[int]
    """Volume size in GiB"""

    source: Required[Literal["new"]]

    type: Required[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
    """Volume type"""

    delete_on_termination: bool
    """Flag indicating whether the volume is deleted on instance termination"""

    tags: Dict[str, str]
    """Tags associated with the volume"""


class ServersSettingsVolumeImageVolumeInputSerializer(TypedDict, total=False):
    boot_index: Required[int]
    """Boot index of the volume"""

    image_id: Required[str]
    """Image ID for the volume"""

    name: Required[str]
    """Volume name"""

    size: Required[int]
    """Volume size in GiB"""

    source: Required[Literal["image"]]

    type: Required[Literal["cold", "ssd_hiiops", "ssd_local", "ssd_lowlatency", "standard", "ultra"]]
    """Volume type"""

    delete_on_termination: bool
    """Flag indicating whether the volume is deleted on instance termination"""

    tags: Dict[str, str]
    """Tags associated with the volume"""


ServersSettingsVolume: TypeAlias = Union[
    ServersSettingsVolumeNewVolumeInputSerializer, ServersSettingsVolumeImageVolumeInputSerializer
]


class ServersSettings(TypedDict, total=False):
    """Configuration settings for the servers in the cluster"""

    credentials: ServersSettingsCredentials
    """Optional server access credentials"""

    user_data: str
    """Optional custom user data (Base64-encoded)"""

    volumes: Iterable[ServersSettingsVolume]
    """List of volumes"""
