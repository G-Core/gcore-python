# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["S3StorageCreated", "AccessKey"]


class AccessKey(BaseModel):
    access_key: str
    """Access key ID used as the username in S3 authentication.

    Pass this in the `AWS_ACCESS_KEY_ID` field of your S3 client.
    """

    secret_key: str
    """Secret key used as the password in S3 authentication.

    Save this now — it cannot be retrieved again.
    """


class S3StorageCreated(BaseModel):
    id: int
    """Unique identifier for the storage instance"""

    access_keys: List[AccessKey]
    """S3 access keys"""

    address: str
    """Full hostname/address for accessing the storage endpoint"""

    created_at: datetime
    """ISO 8601 timestamp when the storage was created"""

    full_name: str
    """
    Read-only internal full name of the storage, composed as "{`client_id`}-{name}".
    Used internally by the backend. Clients should continue to identify the storage
    by `name`.
    """

    location_name: str
    """Geographic location code where the storage is provisioned"""

    name: str
    """User-defined name for the storage instance, as supplied at creation time."""

    provisioning_status: Literal["creating", "active", "updating", "deleting", "deleted"]
    """Lifecycle status of the storage. Use this to check readiness before operations."""
