# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .binary_short import BinaryShort

__all__ = ["BinaryListResponse"]


class BinaryListResponse(BaseModel):
    binaries: List[BinaryShort]
