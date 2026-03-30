# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["Bucket", "Cors", "Lifecycle", "Policy"]


class Cors(BaseModel):
    allowed_origins: List[str]
    """
    Web domains allowed to make direct browser requests to this bucket (e.g.,
    "https://myapp.com"). Use "\\**" to allow any origin.
    """


class Lifecycle(BaseModel):
    expiration_days: int
    """Days after upload before objects are automatically deleted.

    For example, 30 means files are removed 30 days after creation.
    """


class Policy(BaseModel):
    is_public: bool
    """When true, anyone can download objects without credentials.

    When false, all requests require valid S3 authentication.
    """


class Bucket(BaseModel):
    cors: Cors

    lifecycle: Lifecycle

    name: str
    """Globally unique bucket name within the storage.

    Used as the path prefix when accessing objects via S3 API.
    """

    policy: Policy

    storage_id: int
    """Parent storage this bucket belongs to.

    Use this ID in the URL path for bucket operations.
    """
