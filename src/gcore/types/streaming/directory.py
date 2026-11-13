# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .directory_detail import DirectoryDetail

__all__ = ["Directory"]


class Directory(BaseModel):
    directory: Optional[DirectoryDetail] = None
