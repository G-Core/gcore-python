# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ClusterUpdateServersSettingsParams", "ServersSettings", "ServersSettingsCredentials"]


class ClusterUpdateServersSettingsParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    image_id: str
    """System image ID"""

    servers_settings: ServersSettings
    """Configuration settings for the servers in the cluster"""


class ServersSettingsCredentials(TypedDict, total=False):
    """Optional server access credentials.

    Omit the field to leave it unchanged, or set it to `null` to clear the currently stored value.
    """

    ssh_key_name: str
    """
    Specifies the name of the SSH keypair, created via the
    [/v1/`ssh_keys` endpoint](/docs/api-reference/cloud/ssh-keys/add-or-generate-ssh-key).
    """


class ServersSettings(TypedDict, total=False):
    """Configuration settings for the servers in the cluster"""

    credentials: Optional[ServersSettingsCredentials]
    """Optional server access credentials.

    Omit the field to leave it unchanged, or set it to `null` to clear the currently
    stored value.
    """

    user_data: Optional[str]
    """Optional custom user data (Base64-encoded).

    Omit the field to leave it unchanged, or set it to `null` to clear the currently
    stored value.
    """
