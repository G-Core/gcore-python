# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["KvStoreShort"]


class KvStoreShort(BaseModel):
    id: int
    """The unique identifier of the store"""

    app_count: int
    """The number of applications that use this store"""

    name: str
    """A name of the store"""

    comment: Optional[str] = None
    """A description of the store"""

    size: Optional[int] = None
    """Total store size in bytes"""
