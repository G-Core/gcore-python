# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .directory_base import DirectoryBase
from .directory_item import DirectoryItem
from .directory_video import DirectoryVideo

__all__ = ["DirectoryDetail", "DirectoryDetailItem"]

DirectoryDetailItem: TypeAlias = Union[DirectoryVideo, DirectoryItem]


class DirectoryDetail(DirectoryBase):
    items: Optional[List[DirectoryDetailItem]] = None
    """Contents of the directory, subdirectories and videos in one list.

    Empty array if the directory is empty.
    """
