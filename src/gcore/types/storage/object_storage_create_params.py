# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ObjectStorageCreateParams"]


class ObjectStorageCreateParams(TypedDict, total=False):
    location_name: Required[str]
    """Location code where the storage should be created"""

    name: Required[str]
    """User-defined name for the storage instance"""

    accept_language: Annotated[str, PropertyInfo(alias="Accept-Language")]
