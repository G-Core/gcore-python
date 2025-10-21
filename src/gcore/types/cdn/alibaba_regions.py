# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["AlibabaRegions", "AlibabaRegionItem"]


class AlibabaRegionItem(BaseModel):
    id: Optional[int] = None
    """Region ID."""

    code: Optional[str] = None
    """Region code."""

    name: Optional[str] = None
    """Region name."""


AlibabaRegions: TypeAlias = List[AlibabaRegionItem]
