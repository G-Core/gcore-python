# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .secret import Secret
from ..._models import BaseModel

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    count: int
    """
    '#/components/schemas/SecretSerializerList/properties/count'
    "$.components.schemas.SecretSerializerList.properties.count"
    """

    results: List[Secret]
    """
    '#/components/schemas/SecretSerializerList/properties/results'
    "$.components.schemas.SecretSerializerList.properties.results"
    """
