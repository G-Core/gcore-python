# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .registry_artifact import RegistryArtifact

__all__ = ["RegistryArtifactList"]


class RegistryArtifactList(BaseModel):
    count: int
    """Number of objects"""

    results: List[RegistryArtifact]
    """Objects"""
