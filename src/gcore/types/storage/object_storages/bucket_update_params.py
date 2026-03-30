# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["BucketUpdateParams", "Cors", "Lifecycle", "Policy"]


class BucketUpdateParams(TypedDict, total=False):
    storage_id: Required[int]

    cors: Cors

    lifecycle: Lifecycle

    policy: Policy


class Cors(TypedDict, total=False):
    allowed_origins: SequenceNotStr[str]
    """Web domains allowed to make direct browser requests.

    Send an empty array to remove CORS configuration.
    """


class Lifecycle(TypedDict, total=False):
    expiration_days: int
    """Days before objects are automatically deleted.

    Set to a positive number to enable, or null/0 to remove the rule.
    """


class Policy(TypedDict, total=False):
    is_public: bool
    """
    Set to true to allow unauthenticated object downloads, false to require valid S3
    credentials.
    """
