# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .waap_ddos_attack import WaapDDOSAttack

__all__ = ["WaapPaginatedDDOSAttack"]


class WaapPaginatedDDOSAttack(BaseModel):
    count: int
    """Number of items contain in the response"""

    limit: int
    """Number of items requested in the response"""

    offset: int
    """Items response offset used"""

    results: List[WaapDDOSAttack]
    """List of items returned in the response following given criteria"""
