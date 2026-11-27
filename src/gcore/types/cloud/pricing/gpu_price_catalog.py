# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .gpu_price import GPUPrice
from ...._models import BaseModel

__all__ = ["GPUPriceCatalog"]


class GPUPriceCatalog(BaseModel):
    count: int
    """Number of objects"""

    generated_at: datetime
    """When this catalog snapshot was built."""

    results: List[GPUPrice]
    """Objects"""
