# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FlavorHardwareDescription"]


class FlavorHardwareDescription(BaseModel):
    cpu: Optional[str] = None
    """Human-readable CPU description"""

    disk: Optional[str] = None
    """Human-readable disk description"""

    ephemeral: Optional[str] = None
    """Human-readable ephemeral disk description"""

    gpu: Optional[str] = None
    """Human-readable GPU description"""

    network: Optional[str] = None
    """Human-readable NIC description"""

    ram: Optional[str] = None
    """Human-readable RAM description"""
