# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["RegistryUser"]


class RegistryUser(BaseModel):
    id: int
    """
    '#/components/schemas/RegistryUserSerializer/properties/id'
    "$.components.schemas.RegistryUserSerializer.properties.id"
    """

    created_at: datetime
    """
    '#/components/schemas/RegistryUserSerializer/properties/created_at'
    "$.components.schemas.RegistryUserSerializer.properties.created_at"
    """

    duration: int
    """
    '#/components/schemas/RegistryUserSerializer/properties/duration'
    "$.components.schemas.RegistryUserSerializer.properties.duration"
    """

    expires_at: datetime
    """
    '#/components/schemas/RegistryUserSerializer/properties/expires_at'
    "$.components.schemas.RegistryUserSerializer.properties.expires_at"
    """

    name: str
    """
    '#/components/schemas/RegistryUserSerializer/properties/name'
    "$.components.schemas.RegistryUserSerializer.properties.name"
    """

    read_only: Optional[bool] = None
    """
    '#/components/schemas/RegistryUserSerializer/properties/read_only'
    "$.components.schemas.RegistryUserSerializer.properties.read_only"
    """
