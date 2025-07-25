# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .video import Video

__all__ = ["DirectoryVideo"]


class DirectoryVideo(Video):
    item_type: Optional[Literal["Video"]] = None
    """Type of the entity: directory, or video"""
