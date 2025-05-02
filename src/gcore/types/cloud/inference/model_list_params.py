# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .mlcatalog_order_by_choices import MlcatalogOrderByChoices

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """

    order_by: MlcatalogOrderByChoices
    """Order instances by transmitted fields and directions"""
