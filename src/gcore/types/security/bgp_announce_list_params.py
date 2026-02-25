# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["BgpAnnounceListParams"]


class BgpAnnounceListParams(TypedDict, total=False):
    announced: Optional[bool]

    client_id: Optional[int]
    """A positive integer ID"""

    limit: Optional[int]

    offset: Optional[int]

    origin: Optional[List[Literal["STATIC", "DYNAMIC", "IAAS", "PROTECTED_NETWORK", "EDGE_PROXY"]]]

    site: Optional[str]
