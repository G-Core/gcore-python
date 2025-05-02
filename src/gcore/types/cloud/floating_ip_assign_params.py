# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FloatingIPAssignParams"]


class FloatingIPAssignParams(TypedDict, total=False):
    project_id: int

    region_id: int

    port_id: Required[str]
    """Port ID"""

    fixed_ip_address: Optional[str]
    """Fixed IP address"""
