# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .image import Image
from ..._models import BaseModel

__all__ = ["ImageList"]


class ImageList(BaseModel):
    count: int
    """
    '#/components/schemas/ImageCollectionSerializer/properties/count'
    "$.components.schemas.ImageCollectionSerializer.properties.count"
    """

    results: List[Image]
    """
    '#/components/schemas/ImageCollectionSerializer/properties/results'
    "$.components.schemas.ImageCollectionSerializer.properties.results"
    """
