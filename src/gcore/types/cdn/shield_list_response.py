# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ShieldListResponse", "ShieldListResponseItem"]


class ShieldListResponseItem(BaseModel):
    id: Optional[int] = None
    """Origin shielding location ID."""

    city: Optional[str] = None
    """City of origin shielding location."""

    country: Optional[str] = None
    """Country of origin shielding location."""

    datacenter: Optional[str] = None
    """Name of origin shielding location datacenter."""


ShieldListResponse: TypeAlias = List[ShieldListResponseItem]
