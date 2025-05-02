# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .secret import Secret
from ..._models import BaseModel

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[Secret]
    """Objects"""
