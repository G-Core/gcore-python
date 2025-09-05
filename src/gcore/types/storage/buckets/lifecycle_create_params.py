# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LifecycleCreateParams"]


class LifecycleCreateParams(TypedDict, total=False):
    storage_id: Required[int]

    expiration_days: int
