# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["RegistryUser"]


class RegistryUser(BaseModel):
    id: int
    """User ID"""

    created_at: datetime
    """User creation date-time"""

    duration: int
    """User account operating time, days"""

    expires_at: datetime
    """User operation end date-time"""

    name: str
    """User name"""

    read_only: Optional[bool] = None
    """Read-only user"""
