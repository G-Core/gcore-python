# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectStorageCreateParams"]


class ObjectStorageCreateParams(TypedDict, total=False):
    location_name: Required[str]
    """Location code where the storage should be created"""

    name: Required[str]
    """User-defined name for the storage instance"""
