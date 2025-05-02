# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["RegistryTag"]


class RegistryTag(BaseModel):
    id: int
    """Tag ID"""

    artifact_id: int
    """Artifact ID"""

    name: str
    """Tag name"""

    pulled_at: datetime
    """Tag last pull date-time"""

    pushed_at: datetime
    """Tag push date-time"""

    repository_id: int
    """Repository ID"""
