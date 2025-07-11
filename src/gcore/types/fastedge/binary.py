# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Binary"]


class Binary(BaseModel):
    id: int
    """Binary ID"""

    api_type: str
    """Wasm API type"""

    source: int
    """
    Source language:
    0 - unknown
    1 - Rust
    2 - JavaScript
    """

    status: int
    """
    Status code:
    0 - pending
    1 - compiled
    2 - compilation failed (errors available)
    3 - compilation failed (errors not available)
    4 - resulting binary exceeded the limit
    5 - unsupported source language
    """

    checksum: Optional[str] = None
    """MD5 hash of the binary"""

    unref_since: Optional[str] = None
    """Not used since (UTC)"""
