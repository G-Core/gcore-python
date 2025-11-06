# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["BgpAnnounceListParams"]


class BgpAnnounceListParams(TypedDict, total=False):
    announced: Optional[bool]

    origin: Optional[Literal["STATIC", "DYNAMIC"]]

    site: Optional[str]
