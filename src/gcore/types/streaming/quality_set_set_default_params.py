# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["QualitySetSetDefaultParams", "Live", "Vod"]


class QualitySetSetDefaultParams(TypedDict, total=False):
    live: Live

    vod: Vod


class Live(TypedDict, total=False):
    id: int
    """ID of the custom quality set, or "null" for the system default"""


class Vod(TypedDict, total=False):
    id: int
    """ID of the custom quality set, or "null" for the system default"""
