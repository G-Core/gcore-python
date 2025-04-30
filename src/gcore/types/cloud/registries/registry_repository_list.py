# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .registry_repository import RegistryRepository

__all__ = ["RegistryRepositoryList"]


class RegistryRepositoryList(BaseModel):
    count: int
    """
    '#/components/schemas/RegistryRepositoryCollectionSerializer/properties/count'
    "$.components.schemas.RegistryRepositoryCollectionSerializer.properties.count"
    """

    results: List[RegistryRepository]
    """
    '#/components/schemas/RegistryRepositoryCollectionSerializer/properties/results'
    "$.components.schemas.RegistryRepositoryCollectionSerializer.properties.results"
    """
