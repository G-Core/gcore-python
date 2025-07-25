# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .directory_base import DirectoryBase

__all__ = ["DirectoryItem"]


class DirectoryItem(DirectoryBase):
    item_type: Optional[Literal["Directory"]] = None
    """Type of the entity: directory, or video"""
