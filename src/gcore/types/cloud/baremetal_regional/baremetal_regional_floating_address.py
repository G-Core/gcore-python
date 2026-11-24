# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BaremetalRegionalFloatingAddress"]


class BaremetalRegionalFloatingAddress(BaseModel):
    addr: str
    """Address"""

    type: Literal["floating"]
    """Type of the address"""
