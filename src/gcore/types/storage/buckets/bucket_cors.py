# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BucketCors"]


class BucketCors(BaseModel):
    """StorageGetBucketCorsEndpointRes output"""

    allowed_origins: Optional[List[str]] = FieldInfo(alias="allowedOrigins", default=None)
    """
    List of allowed origins for Cross-Origin Resource Sharing (CORS) requests.
    Contains domains/URLs that are permitted to make cross-origin requests to this
    bucket.
    """
