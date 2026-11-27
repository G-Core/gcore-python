# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel

__all__ = ["GPUPriceDetail"]


class GPUPriceDetail(BaseModel):
    flavor_names: List[str]
    """Flavor names that share this SKU and price."""

    sku: str
    """SKU id for this price row."""

    updated_at: datetime
    """When this row was last refreshed."""
