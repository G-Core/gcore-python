# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .kv_store import KvStore

__all__ = ["KvStoreCreateResponse"]


class KvStoreCreateResponse(KvStore):
    id: Optional[int] = None
    """The unique identifier of the store."""
