# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PublicNetworkList"]


class PublicNetworkList(BaseModel):
    addresses: Optional[List[str]] = None
    """List of IPv4 networks."""

    addresses_v6: Optional[List[str]] = None
    """List of IPv6 networks."""
