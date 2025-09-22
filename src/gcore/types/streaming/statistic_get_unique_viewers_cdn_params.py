# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatisticGetUniqueViewersCdnParams"]


class StatisticGetUniqueViewersCdnParams(TypedDict, total=False):
    date_from: Required[str]
    """Start of time frame. Format is date time in ISO 8601."""

    date_to: Required[str]
    """End of time frame. Format is date time in ISO 8601."""

    id: str
    """Filter by entity's id.

    Put ID of a Live stream, VOD or a playlist to be calculated.

    If the value is omitted, then the calculation is done for all videos/streams of
    the specified type.

    When using this "id" parameter, be sure to specify the "type" parameter too. If
    you do not specify a type, the "id" will be ignored.
    """

    type: Literal["live", "vod", "playlist"]
    """Filter by entity's type"""
