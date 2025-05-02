# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .registry_user import RegistryUser

__all__ = ["RegistryUserList"]


class RegistryUserList(BaseModel):
    count: int
    """Number of objects"""

    results: List[RegistryUser]
    """Objects"""
