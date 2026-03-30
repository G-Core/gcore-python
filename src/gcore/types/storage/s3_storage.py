# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["S3Storage"]


class S3Storage(BaseModel):
    id: int
    """Unique identifier for the storage instance"""

    address: str
    """Full hostname/address for accessing the storage endpoint"""

    created_at: datetime
    """ISO 8601 timestamp when the storage was created"""

    location_name: str
    """Geographic location code where the storage is provisioned"""

    name: str
    """User-defined name for the storage instance"""

    provisioning_status: Literal["creating", "active", "updating", "deleting", "deleted"]
    """Lifecycle status of the storage. Use this to check readiness before operations."""
