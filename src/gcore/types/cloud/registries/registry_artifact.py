# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel
from ..registry_tag import RegistryTag

__all__ = ["RegistryArtifact"]


class RegistryArtifact(BaseModel):
    id: int
    """Repository ID"""

    digest: str
    """Artifact digest"""

    pulled_at: datetime
    """Artifact last pull date-time"""

    pushed_at: datetime
    """Artifact push date-time"""

    registry_id: int
    """Artifact registry ID"""

    repository_id: int
    """Artifact repository ID"""

    size: int
    """Artifact size, bytes"""

    tags: List[RegistryTag]
    """Artifact tags"""
