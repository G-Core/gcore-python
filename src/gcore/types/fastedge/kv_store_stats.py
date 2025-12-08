# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["KvStoreStats", "Stats"]


class Stats(BaseModel):
    """Store statistics"""

    cf_count: int
    """Total number of Cuckoo filter entries"""

    kv_count: int
    """Total number of KV entries"""

    size: int
    """Total store size in bytes"""

    zset_count: int
    """Total number of sorted set entries"""


class KvStoreStats(BaseModel):
    stats: Optional[Stats] = None
    """Store statistics"""
