# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["SftpStorageUpdateParams"]


class SftpStorageUpdateParams(TypedDict, total=False):
    expires: str
    """Duration when the storage should expire (e.g., "2 years 6 months").

    Empty string to remove.
    """

    has_custom_config_file: bool
    """Whether this storage should use a custom configuration file"""

    is_http_disabled: bool
    """Whether HTTP access should be disabled (HTTPS only)"""

    password_mode: Literal["auto", "none"]
    """Password handling mode.

    Omit to leave password unchanged. 'auto': regenerate password (returned in
    response) 'none': remove password Note: 'set' is not allowed in PATCH.
    """

    server_alias: str
    """Custom domain alias for accessing the storage. Empty string to remove."""

    ssh_key_ids: Iterable[int]
    """SSH key IDs to associate with this storage.

    Replaces all existing keys. If omitted, existing keys are unchanged. If empty
    array, all keys are removed.
    """
