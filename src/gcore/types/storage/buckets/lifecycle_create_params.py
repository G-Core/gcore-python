# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LifecycleCreateParams"]


class LifecycleCreateParams(TypedDict, total=False):
    storage_id: Required[int]

    expiration_days: int
    """
    Number of days after which objects will be automatically deleted from the
    bucket. Must be a positive integer. Common values: 30 for monthly cleanup, 365
    for yearly retention.
    """
