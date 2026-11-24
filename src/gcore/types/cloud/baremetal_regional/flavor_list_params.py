# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FlavorListParams"]


class FlavorListParams(TypedDict, total=False):
    project_id: int
    """Project ID"""

    region_id: int
    """Region ID"""

    disabled: bool
    """Flag for filtering disabled flavors in the region"""

    exclude_linux: bool
    """Set to true to exclude flavors dedicated to linux images"""

    exclude_windows: bool
    """Set to true to exclude flavors dedicated to windows images"""

    include_capacity: bool
    """Set to true if the response should include flavor capacity"""

    include_prices: bool
    """Set to true if the response should include flavor prices"""

    include_reservation_stock: bool
    """Optional.

    Set to true if flavor listing should include count of reserved resources in
    stock.
    """

    limit: int
    """Optional. Limit the number of returned items"""

    offset: int
    """Optional.

    Offset value is used to exclude the first set of records from the result
    """
