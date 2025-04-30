# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["Registry"]


class Registry(BaseModel):
    id: int
    """
    '#/components/schemas/RegistrySerializer/properties/id'
    "$.components.schemas.RegistrySerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/RegistrySerializer/properties/created_at'
    "$.components.schemas.RegistrySerializer.properties.created_at"
    """

    name: str
    """
    '#/components/schemas/RegistrySerializer/properties/name'
    "$.components.schemas.RegistrySerializer.properties.name"
    """

    repo_count: int
    """
    '#/components/schemas/RegistrySerializer/properties/repo_count'
    "$.components.schemas.RegistrySerializer.properties.repo_count"
    """

    storage_limit: int
    """
    '#/components/schemas/RegistrySerializer/properties/storage_limit'
    "$.components.schemas.RegistrySerializer.properties.storage_limit"
    """

    storage_used: int
    """
    '#/components/schemas/RegistrySerializer/properties/storage_used'
    "$.components.schemas.RegistrySerializer.properties.storage_used"
    """

    updated_at: datetime
    """
    '#/components/schemas/RegistrySerializer/properties/updated_at'
    "$.components.schemas.RegistrySerializer.properties.updated_at"
    """

    url: str
    """
    '#/components/schemas/RegistrySerializer/properties/url'
    "$.components.schemas.RegistrySerializer.properties.url"
    """
