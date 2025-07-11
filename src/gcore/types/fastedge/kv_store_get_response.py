# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .kv_store import KvStore
from .kv_store_stats import KvStoreStats

__all__ = ["KvStoreGetResponse"]


class KvStoreGetResponse(KvStore, KvStoreStats):
    pass
