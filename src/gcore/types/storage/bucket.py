# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Bucket"]


class Bucket(BaseModel):
    """BucketDtoV2 for response"""

    name: str
    """Name of the S3 bucket"""

    lifecycle: Optional[int] = None
    """Lifecycle policy expiration days (zero if not set)"""
