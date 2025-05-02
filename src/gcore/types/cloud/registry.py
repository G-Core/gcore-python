# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["Registry"]


class Registry(BaseModel):
    id: int
    """Registry ID"""

    created_at: datetime
    """Registry creation date-time"""

    name: str
    """Registry name"""

    repo_count: int
    """Number of repositories in the registry"""

    storage_limit: int
    """Registry storage limit, GiB"""

    storage_used: int
    """Registry storage used, bytes"""

    updated_at: datetime
    """Registry modification date-time"""

    url: str
    """Registry url"""
