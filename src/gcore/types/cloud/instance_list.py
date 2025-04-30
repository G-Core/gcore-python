# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .instance import Instance
from ..._models import BaseModel

__all__ = ["InstanceList"]


class InstanceList(BaseModel):
    count: int
    """
    '#/components/schemas/InstanceCollectionSerializer/properties/count'
    "$.components.schemas.InstanceCollectionSerializer.properties.count"
    """

    results: List[Instance]
    """
    '#/components/schemas/InstanceCollectionSerializer/properties/results'
    "$.components.schemas.InstanceCollectionSerializer.properties.results"
    """
