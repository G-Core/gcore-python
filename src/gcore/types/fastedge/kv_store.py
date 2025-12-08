# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["KvStore", "Byod"]


class Byod(BaseModel):
    """BYOD (Bring Your Own Data) settings"""

    prefix: str
    """Key prefix"""

    url: str
    """URL to connect to"""


class KvStore(BaseModel):
    id: Optional[int] = None
    """The unique identifier of the store"""

    app_count: Optional[int] = None
    """The number of applications that use this store"""

    byod: Optional[Byod] = None
    """BYOD (Bring Your Own Data) settings"""

    comment: Optional[str] = None
    """A description of the store"""

    updated: Optional[datetime] = None
    """Last update time"""
