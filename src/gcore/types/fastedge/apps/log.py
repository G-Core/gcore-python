# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Log"]


class Log(BaseModel):
    id: Optional[str] = None
    """Id of the log"""

    app_name: Optional[str] = None
    """Name of the application"""

    client_ip: Optional[str] = None
    """Client IP"""

    edge: Optional[str] = None
    """Edge name"""

    log: Optional[str] = None
    """Log message"""

    timestamp: Optional[datetime] = None
    """Timestamp of a log in RFC3339 format"""
