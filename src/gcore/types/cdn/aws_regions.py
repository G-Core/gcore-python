# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["AwsRegions", "AwsRegionItem"]


class AwsRegionItem(BaseModel):
    id: Optional[int] = None
    """Region ID."""

    code: Optional[str] = None
    """Region code."""

    name: Optional[str] = None
    """Region name."""


AwsRegions: TypeAlias = List[AwsRegionItem]
