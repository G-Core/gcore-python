# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DDOSProfileOptionList"]


class DDOSProfileOptionList(BaseModel):
    active: Optional[bool] = None
    """Activate profile."""

    bgp: Optional[bool] = None
    """Activate BGP protocol."""
