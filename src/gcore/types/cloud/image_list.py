# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .image import Image
from ..._models import BaseModel

__all__ = ["ImageList"]


class ImageList(BaseModel):
    count: int
    """Number of objects"""

    results: List[Image]
    """Objects"""
