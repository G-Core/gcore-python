# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .image import Image
from ..._models import BaseModel

__all__ = ["ImageList"]


class ImageList(BaseModel):
    count: Optional[int] = None
    """
    '#/components/schemas/ImageListSchema/properties/count'
    "$.components.schemas.ImageListSchema.properties.count"
    """

    results: Optional[List[Image]] = None
    """
    '#/components/schemas/ImageListSchema/properties/results'
    "$.components.schemas.ImageListSchema.properties.results"
    """
