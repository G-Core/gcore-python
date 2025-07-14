# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AppShort"]


class AppShort(BaseModel):
    id: int
    """App ID"""

    api_type: str
    """Wasm API type"""

    binary: int
    """Binary ID"""

    name: str
    """App name"""

    plan_id: int
    """Application plan ID"""

    status: int
    """
    Status code:
    0 - draft (inactive)
    1 - enabled
    2 - disabled
    3 - hourly call limit exceeded
    4 - daily call limit exceeded
    5 - suspended
    """

    comment: Optional[str] = None
    """Description of the binary"""

    debug_until: Optional[datetime] = None
    """When debugging finishes"""

    networks: Optional[List[str]] = None
    """Networks"""

    plan: Optional[str] = None
    """Application plan name"""

    template: Optional[int] = None
    """Template ID"""

    template_name: Optional[str] = None
    """Template name"""

    upgradeable_to: Optional[int] = None
    """ID of the binary the app can be upgraded to"""

    url: Optional[str] = None
    """App URL"""
