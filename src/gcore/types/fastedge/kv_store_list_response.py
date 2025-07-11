# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .kv_store_short import KvStoreShort

__all__ = ["KvStoreListResponse"]


class KvStoreListResponse(BaseModel):
    count: int
    """Total number of stores"""

    stores: Optional[List[KvStoreShort]] = None
