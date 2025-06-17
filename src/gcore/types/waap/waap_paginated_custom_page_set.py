# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .waap_custom_page_set import WaapCustomPageSet

__all__ = ["WaapPaginatedCustomPageSet"]


class WaapPaginatedCustomPageSet(BaseModel):
    count: int
    """Number of items contain in the response"""

    limit: int
    """Number of items requested in the response"""

    offset: int
    """Items response offset used"""

    results: List[WaapCustomPageSet]
    """List of items returned in the response following given criteria"""
