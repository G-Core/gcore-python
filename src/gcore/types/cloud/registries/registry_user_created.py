# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["RegistryUserCreated"]


class RegistryUserCreated(BaseModel):
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

    read_only: bool
    """Read-only user"""

    secret: str
    """User secret"""
