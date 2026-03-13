# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Log"]


class Log(BaseModel):
    id: Optional[str] = None
    """Unique identifier for this log entry"""

    app_name: Optional[str] = None
    """Name of the application that generated this log"""

    client_ip: Optional[str] = None
    """IP address of the client that triggered the log"""

    edge: Optional[str] = None
    """Edge location where the log originated"""

    log: Optional[str] = None
    """The actual log message content"""

    timestamp: Optional[datetime] = None
    """When the log was generated (RFC3339 format)"""
