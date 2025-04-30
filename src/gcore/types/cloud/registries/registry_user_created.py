# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["RegistryUserCreated"]


class RegistryUserCreated(BaseModel):
    id: int
    """
    '#/components/schemas/RegistryUserCreateResponseSerializer/properties/id'
    "$.components.schemas.RegistryUserCreateResponseSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/RegistryUserCreateResponseSerializer/properties/created_at'
    "$.components.schemas.RegistryUserCreateResponseSerializer.properties.created_at"
    """

    duration: int
    """
    '#/components/schemas/RegistryUserCreateResponseSerializer/properties/duration'
    "$.components.schemas.RegistryUserCreateResponseSerializer.properties.duration"
    """

    expires_at: datetime
    """
    '#/components/schemas/RegistryUserCreateResponseSerializer/properties/expires_at'
    "$.components.schemas.RegistryUserCreateResponseSerializer.properties.expires_at"
    """

    name: str
    """
    '#/components/schemas/RegistryUserCreateResponseSerializer/properties/name'
    "$.components.schemas.RegistryUserCreateResponseSerializer.properties.name"
    """

    read_only: Optional[bool] = None
    """
    '#/components/schemas/RegistryUserCreateResponseSerializer/properties/read_only'
    "$.components.schemas.RegistryUserCreateResponseSerializer.properties.read_only"
    """

    secret: Optional[str] = None
    """
    '#/components/schemas/RegistryUserCreateResponseSerializer/properties/secret'
    "$.components.schemas.RegistryUserCreateResponseSerializer.properties.secret"
    """
