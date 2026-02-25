# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BgpAnnounceToggleParams"]


class BgpAnnounceToggleParams(TypedDict, total=False):
    announce: Required[str]
    """IP network to announce"""

    enabled: Required[bool]
    """Whether the announcement is enabled"""

    client_id: Optional[int]
    """A positive integer ID"""
