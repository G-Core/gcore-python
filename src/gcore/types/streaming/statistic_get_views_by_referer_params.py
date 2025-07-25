# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StatisticGetViewsByRefererParams"]


class StatisticGetViewsByRefererParams(TypedDict, total=False):
    date_from: Required[str]
    """Start of time frame. Datetime in ISO 8601 format."""

    date_to: Required[str]
    """End of time frame. Datetime in ISO 8601 format."""
