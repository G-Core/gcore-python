# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from . import directory_item
from ..._models import BaseModel
from .directory_base import DirectoryBase
from .directory_video import DirectoryVideo

__all__ = ["DirectoryGetResponse", "Directory", "DirectoryItem"]

DirectoryItem: TypeAlias = Union[DirectoryVideo, directory_item.DirectoryItem]


class Directory(DirectoryBase):
    items: Optional[List[DirectoryItem]] = None
    """Array of subdirectories, if any."""


class DirectoryGetResponse(BaseModel):
    directory: Optional[Directory] = None
