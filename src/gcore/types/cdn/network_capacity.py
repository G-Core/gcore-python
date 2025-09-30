# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["NetworkCapacity", "NetworkCapacityItem"]


class NetworkCapacityItem(BaseModel):
    capacity: Optional[float] = None
    """Network capacity in Gbit/s."""

    country: Optional[str] = None
    """Country name."""

    country_code: Optional[str] = None
    """ISO country code."""


NetworkCapacity: TypeAlias = List[NetworkCapacityItem]
