# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AccessKeyCreated"]


class AccessKeyCreated(BaseModel):
    access_key: str
    """Access key ID used as the username in S3 authentication.

    Pass this in the `AWS_ACCESS_KEY_ID` field of your S3 client.
    """

    created_at: datetime
    """ISO 8601 timestamp when the access key was created"""

    expires_at: Optional[datetime] = None
    """ISO 8601 timestamp when the key expires, or null for a key that never expires."""

    read_only: bool
    """True for a key scoped to read-only data access."""

    secret_key: str
    """Secret key used as the password in S3 authentication.

    Save this now — it cannot be retrieved again.
    """
