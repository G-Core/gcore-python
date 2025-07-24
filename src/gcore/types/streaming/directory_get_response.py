# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel
from .directory_base import DirectoryBase
from .directory_item import DirectoryItem
from .directory_video import DirectoryVideo

__all__ = ["DirectoryGetResponse", "Directory"]


class Directory(DirectoryBase):
    items: Optional[List[Union[DirectoryVideo, DirectoryItem]]] = None
    """Array of subdirectories, if any."""


class DirectoryGetResponse(BaseModel):
    directory: Optional[Directory] = None
