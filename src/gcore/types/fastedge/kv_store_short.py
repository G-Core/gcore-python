# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["KvStoreShort"]


class KvStoreShort(BaseModel):
    id: Optional[int] = None
    """The unique identifier of the store"""

    comment: Optional[str] = None
    """A description of the store"""

    updated: Optional[datetime] = None
    """Last update time"""
