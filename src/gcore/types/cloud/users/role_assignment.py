# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["RoleAssignment"]


class RoleAssignment(BaseModel):
    id: int
    """Assignment ID"""

    assigned_by: Optional[int] = None

    client_id: int
    """Client ID"""

    created_at: datetime
    """Created timestamp"""

    project_id: Optional[int] = None
    """Project ID"""

    role: str
    """User role"""

    updated_at: Optional[datetime] = None
    """Updated timestamp"""

    user_id: int
    """User ID"""
