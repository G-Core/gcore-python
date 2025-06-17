# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .waap_request_summary import WaapRequestSummary

__all__ = ["WaapPaginatedRequestSummary"]


class WaapPaginatedRequestSummary(BaseModel):
    count: int
    """Number of items contain in the response"""

    limit: int
    """Number of items requested in the response"""

    offset: int
    """Items response offset used"""

    results: List[WaapRequestSummary]
    """List of items returned in the response following given criteria"""
