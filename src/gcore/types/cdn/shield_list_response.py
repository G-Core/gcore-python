# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ShieldListResponse"]


class ShieldListResponse(BaseModel):
    id: Optional[int] = None
    """Origin shielding location ID."""

    city: Optional[str] = None
    """City of origin shielding location."""

    country: Optional[str] = None
    """Country of origin shielding location."""

    datacenter: Optional[str] = None
    """Name of origin shielding location datacenter."""
