# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["KvStoreListParams"]


class KvStoreListParams(TypedDict, total=False):
    app_id: int
    """Filter stores by application ID. Returns only stores associated with this app."""

    limit: int
    """Maximum number of stores to return per page"""

    offset: int
    """Number of stores to skip for pagination"""
