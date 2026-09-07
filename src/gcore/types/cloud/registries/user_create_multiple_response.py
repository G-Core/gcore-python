# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .registry_user_created import RegistryUserCreated

__all__ = ["UserCreateMultipleResponse"]


class UserCreateMultipleResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[RegistryUserCreated]
    """Objects"""
