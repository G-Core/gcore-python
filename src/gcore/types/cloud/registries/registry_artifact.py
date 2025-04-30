# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel
from ..registry_tag import RegistryTag

__all__ = ["RegistryArtifact"]


class RegistryArtifact(BaseModel):
    id: int
    """
    '#/components/schemas/RegistryArtifactSerializer/properties/id'
    "$.components.schemas.RegistryArtifactSerializer.properties.id"
    """

    digest: str
    """
    '#/components/schemas/RegistryArtifactSerializer/properties/digest'
    "$.components.schemas.RegistryArtifactSerializer.properties.digest"
    """

    pulled_at: datetime
    """
    '#/components/schemas/RegistryArtifactSerializer/properties/pulled_at'
    "$.components.schemas.RegistryArtifactSerializer.properties.pulled_at"
    """

    pushed_at: datetime
    """
    '#/components/schemas/RegistryArtifactSerializer/properties/pushed_at'
    "$.components.schemas.RegistryArtifactSerializer.properties.pushed_at"
    """

    registry_id: int
    """
    '#/components/schemas/RegistryArtifactSerializer/properties/registry_id'
    "$.components.schemas.RegistryArtifactSerializer.properties.registry_id"
    """

    repository_id: int
    """
    '#/components/schemas/RegistryArtifactSerializer/properties/repository_id'
    "$.components.schemas.RegistryArtifactSerializer.properties.repository_id"
    """

    size: int
    """
    '#/components/schemas/RegistryArtifactSerializer/properties/size'
    "$.components.schemas.RegistryArtifactSerializer.properties.size"
    """

    tags: List[RegistryTag]
    """
    '#/components/schemas/RegistryArtifactSerializer/properties/tags'
    "$.components.schemas.RegistryArtifactSerializer.properties.tags"
    """
