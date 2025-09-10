# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StorageUpdateParams"]


class StorageUpdateParams(TypedDict, total=False):
    expires: str
    """
    Duration when the storage should expire in format like "2 years 6 months 2 weeks
    3 days 5 hours 10 minutes 15 seconds". Leave empty to remove expiration.
    """

    server_alias: str
    """Custom domain alias for accessing the storage. Leave empty to remove alias."""
