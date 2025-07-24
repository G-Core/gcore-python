# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatisticGetVodStorageVolumeParams"]


class StatisticGetVodStorageVolumeParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Start of time frame. Datetime in ISO 8601 format."""

    to: Required[str]
    """End of time frame. Datetime in ISO 8601 format."""
