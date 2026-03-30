# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SftpStorageCreateParams"]


class SftpStorageCreateParams(TypedDict, total=False):
    location_name: Required[str]
    """Location code where the storage should be created"""

    name: Required[str]
    """User-defined name for the storage instance"""

    password_mode: Required[Literal["auto", "set", "none"]]
    """
    Password handling mode for SFTP access: 'auto': generate a random password
    (returned in the response) 'set': use the password provided in `sftp_password`
    'none': no password (SSH-key-only access)
    """

    expires: str
    """Duration when the storage should expire (e.g., "2 years 6 months").

    Omit for no expiration.
    """

    has_custom_config_file: bool
    """Whether this storage should use a custom configuration file"""

    is_http_disabled: bool
    """Whether HTTP access should be disabled (HTTPS only)"""

    server_alias: str
    """Custom domain alias for accessing the storage. Omit for no alias."""

    sftp_password: str
    """SFTP password (8-63 chars).

    Required when `password_mode` is 'set'. Must be omitted when `password_mode` is
    'auto' or 'none'.
    """

    ssh_key_ids: Iterable[int]
    """SSH key IDs to associate with this storage at creation time.

    If omitted, no keys are linked.
    """
