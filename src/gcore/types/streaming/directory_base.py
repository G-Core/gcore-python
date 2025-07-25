# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DirectoryBase"]


class DirectoryBase(BaseModel):
    id: Optional[int] = None
    """ID of the directory"""

    created_at: Optional[str] = None
    """Time of creation. Datetime in ISO 8601 format."""

    items_count: Optional[int] = None
    """Number of objects in this directory.

    Counting files and folders. The quantity is calculated only at one level (not
    recursively in all subfolders).
    """

    name: Optional[str] = None
    """Title of the directory"""

    parent_id: Optional[int] = None
    """ID of a parent directory. "null" if it's in the root."""

    updated_at: Optional[str] = None
    """Time of last update of the directory entity. Datetime in ISO 8601 format."""
