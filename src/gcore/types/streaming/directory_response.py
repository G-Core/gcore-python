# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .directory_base import DirectoryBase

__all__ = ["DirectoryResponse"]


class DirectoryResponse(BaseModel):
    """Response of the create directory method.

    The directory object is wrapped in the "directory" key.
    """

    directory: Optional[DirectoryBase] = None
