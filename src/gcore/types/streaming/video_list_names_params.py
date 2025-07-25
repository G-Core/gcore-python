# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["VideoListNamesParams"]


class VideoListNamesParams(TypedDict, total=False):
    ids: Iterable[int]
    """Comma-separated set of video IDs. Example, ?ids=7,17"""
