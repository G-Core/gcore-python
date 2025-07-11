# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Client", "Network"]


class Network(BaseModel):
    is_default: bool
    """Is network is default"""

    name: str
    """Network name"""


class Client(BaseModel):
    app_count: int
    """Actual allowed number of apps"""

    app_limit: int
    """Max allowed number of apps"""

    daily_consumption: int
    """Actual number of calls for all apps during the current day (UTC)"""

    daily_limit: int
    """Max allowed calls for all apps during a day (UTC)"""

    hourly_consumption: int
    """Actual number of calls for all apps during the current hour"""

    hourly_limit: int
    """Max allowed calls for all apps during an hour"""

    monthly_consumption: int
    """Actual number of calls for all apps during the current calendar month (UTC)"""

    networks: List[Network]
    """List of enabled networks"""

    plan_id: int
    """Plan ID"""

    status: int
    """
    Status code:
    1 - enabled
    2 - disabled
    3 - hourly call limit exceeded
    4 - daily call limit exceeded
    5 - suspended
    """

    plan: Optional[str] = None
    """Plan name"""
