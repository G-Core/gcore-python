# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .billing_reservation import BillingReservation

__all__ = ["BillingReservations"]


class BillingReservations(BaseModel):
    count: int
    """Number of objects"""

    results: List[BillingReservation]
    """Objects"""
