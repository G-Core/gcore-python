# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RegionListParams"]


class RegionListParams(TypedDict, total=False):
    limit: int
    """Limit the number of returned regions.

    Falls back to default of 100 if not specified. Limited by max limit value of
    1000
    """

    offset: int
    """Offset value is used to exclude the first set of records from the result"""

    order_by: Literal["created_at.asc", "created_at.desc", "display_name.asc", "display_name.desc"]
    """Order by field and direction."""

    product: Literal["containers", "inference"]
    """If defined then return only regions that support given product."""

    show_volume_types: bool
    """
    If true, null `available_volume_type` is replaced with a list of available
    volume types.
    """
