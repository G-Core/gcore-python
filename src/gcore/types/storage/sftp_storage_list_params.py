# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SftpStorageListParams"]


class SftpStorageListParams(TypedDict, total=False):
    id: str
    """Filter by storage ID"""

    limit: int
    """Max number of records in response"""

    location_name: str
    """Filter by storage location/region"""

    name: str
    """Filter by storage name"""

    offset: int
    """Number of records to skip"""

    order_by: str

    provisioning_status: Literal["active", "creating", "updating", "deleting", "deleted"]
    """Filter by provisioning status"""

    show_deleted: bool
    """Include deleted storages"""
