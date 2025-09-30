# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PublicIPList"]


class PublicIPList(BaseModel):
    addresses: Optional[List[str]] = None
    """List of IPv4 addresses."""

    addresses_v6: Optional[List[str]] = None
    """List of IPv6 addresses."""
