# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .registry_repository import RegistryRepository

__all__ = ["RegistryRepositoryList"]


class RegistryRepositoryList(BaseModel):
    count: int
    """Number of objects"""

    results: List[RegistryRepository]
    """Objects"""
