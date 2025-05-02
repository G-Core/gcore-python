# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .registry import Registry
from ..._models import BaseModel

__all__ = ["RegistryList"]


class RegistryList(BaseModel):
    count: int
    """Number of objects"""

    results: List[Registry]
    """Objects"""
