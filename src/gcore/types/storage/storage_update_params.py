# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StorageUpdateParams"]


class StorageUpdateParams(TypedDict, total=False):
    expires: str
    """ISO 8601 timestamp when the storage should expire.

    Leave empty to remove expiration.
    """

    server_alias: str
    """Custom domain alias for accessing the storage. Leave empty to remove alias."""
