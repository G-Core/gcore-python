# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AccessKey"]


class AccessKey(BaseModel):
    access_key: str
    """Access key ID used as the username in S3 authentication.

    Pass this in the `AWS_ACCESS_KEY_ID` field of your S3 client configuration.
    """

    created_at: datetime
    """ISO 8601 timestamp when the access key was created"""

    expires_at: Optional[datetime] = None
    """ISO 8601 timestamp when the key expires, or null for a key that never expires."""

    read_only: bool
    """True for a key scoped to read-only data access."""

    valid: bool
    """
    False once the key's `expires_at` has passed; the key is removed by the
    background cleanup shortly afterwards. Always true for a key with no expiry. A
    key that does not exist returns 404, so false never means "missing". Reflects
    the cached state, not a live backend check.
    """
