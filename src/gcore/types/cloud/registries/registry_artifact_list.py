# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .registry_artifact import RegistryArtifact

__all__ = ["RegistryArtifactList"]


class RegistryArtifactList(BaseModel):
    count: int
    """
    '#/components/schemas/RegistryArtifactCollectionSerializer/properties/count'
    "$.components.schemas.RegistryArtifactCollectionSerializer.properties.count"
    """

    results: List[RegistryArtifact]
    """
    '#/components/schemas/RegistryArtifactCollectionSerializer/properties/results'
    "$.components.schemas.RegistryArtifactCollectionSerializer.properties.results"
    """
