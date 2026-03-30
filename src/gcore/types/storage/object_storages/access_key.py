# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
