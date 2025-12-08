# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KvStoreReplaceParams", "Byod"]


class KvStoreReplaceParams(TypedDict, total=False):
    byod: Byod
    """BYOD (Bring Your Own Data) settings"""

    comment: str
    """A description of the store"""


class Byod(TypedDict, total=False):
    """BYOD (Bring Your Own Data) settings"""

    prefix: Required[str]
    """Key prefix"""

    url: Required[str]
    """URL to connect to"""
