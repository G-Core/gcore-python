# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["RegistryTag"]


class RegistryTag(BaseModel):
    id: int
    """
    '#/components/schemas/RegistryTagSerializer/properties/id'
    "$.components.schemas.RegistryTagSerializer.properties.id"
    """

    artifact_id: int
    """
    '#/components/schemas/RegistryTagSerializer/properties/artifact_id'
    "$.components.schemas.RegistryTagSerializer.properties.artifact_id"
    """

    name: str
    """
    '#/components/schemas/RegistryTagSerializer/properties/name'
    "$.components.schemas.RegistryTagSerializer.properties.name"
    """

    pulled_at: datetime
    """
    '#/components/schemas/RegistryTagSerializer/properties/pulled_at'
    "$.components.schemas.RegistryTagSerializer.properties.pulled_at"
    """

    pushed_at: datetime
    """
    '#/components/schemas/RegistryTagSerializer/properties/pushed_at'
    "$.components.schemas.RegistryTagSerializer.properties.pushed_at"
    """

    repository_id: int
    """
    '#/components/schemas/RegistryTagSerializer/properties/repository_id'
    "$.components.schemas.RegistryTagSerializer.properties.repository_id"
    """
