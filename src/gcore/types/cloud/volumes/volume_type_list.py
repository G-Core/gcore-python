# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .volume_type import VolumeType

__all__ = ["VolumeTypeList"]


class VolumeTypeList(BaseModel):
    count: int
    """Number of objects"""

    results: List[VolumeType]
    """Objects"""
