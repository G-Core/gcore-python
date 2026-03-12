# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .secret_short import SecretShort

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    count: int
    """Total number of secrets matching the filters"""

    secrets: List[SecretShort]
