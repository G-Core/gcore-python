# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["RegistryRepository"]


class RegistryRepository(BaseModel):
    id: int
    """
    '#/components/schemas/RegistryRepositorySerializer/properties/id'
    "$.components.schemas.RegistryRepositorySerializer.properties.id"
    """

    artifact_count: int
    """
    '#/components/schemas/RegistryRepositorySerializer/properties/artifact_count'
    "$.components.schemas.RegistryRepositorySerializer.properties.artifact_count"
    """

    created_at: datetime
    """
    '#/components/schemas/RegistryRepositorySerializer/properties/created_at'
    "$.components.schemas.RegistryRepositorySerializer.properties.created_at"
    """

    name: str
    """
    '#/components/schemas/RegistryRepositorySerializer/properties/name'
    "$.components.schemas.RegistryRepositorySerializer.properties.name"
    """

    pull_count: int
    """
    '#/components/schemas/RegistryRepositorySerializer/properties/pull_count'
    "$.components.schemas.RegistryRepositorySerializer.properties.pull_count"
    """

    registry_id: int
    """
    '#/components/schemas/RegistryRepositorySerializer/properties/registry_id'
    "$.components.schemas.RegistryRepositorySerializer.properties.registry_id"
    """

    updated_at: datetime
    """
    '#/components/schemas/RegistryRepositorySerializer/properties/updated_at'
    "$.components.schemas.RegistryRepositorySerializer.properties.updated_at"
    """
