# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["RegistryRepository"]


class RegistryRepository(BaseModel):
    id: int
    """Repository ID"""

    artifact_count: int
    """Number of artifacts in the repository"""

    created_at: datetime
    """Repository creation date-time"""

    name: str
    """Repository name"""

    pull_count: int
    """Number of pools from the repository"""

    registry_id: int
    """Repository registry ID"""

    updated_at: datetime
    """Repository modification date-time"""
