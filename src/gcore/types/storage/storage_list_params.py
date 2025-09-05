# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["StorageListParams"]


class StorageListParams(TypedDict, total=False):
    id: str
    """Filter by storage ID"""

    limit: int
    """Max number of records in response"""

    location: str
    """Filter by storage location/region"""

    name: str
    """Filter by storage name (exact match)"""

    offset: int
    """Number of records to skip before beginning to write in response."""

    order_by: str
    """Field name to sort by"""

    order_direction: Literal["asc", "desc"]
    """Ascending or descending order"""

    show_deleted: bool
    """Include deleted storages in the response"""

    status: Literal["active", "suspended", "deleted", "pending"]
    """Filter by storage status"""

    type: Literal["s3", "sftp"]
    """Filter by storage type"""
