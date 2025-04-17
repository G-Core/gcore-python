# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["IPRanges"]


class IPRanges(BaseModel):
    ranges: List[str]
    """IP ranges list"""
