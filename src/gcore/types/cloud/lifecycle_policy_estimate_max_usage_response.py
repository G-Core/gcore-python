# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LifecyclePolicyEstimateMaxUsageResponse", "MaxCost"]


class MaxCost(BaseModel):
    """Total billed cost of all snapshots that can be created by the schedule.

    Cost of `max_volume_snapshot_count_usage` snapshots.
    """

    currency_code: Optional[Literal["AZN", "EUR", "USD"]] = None
    """Currency code (3 letter code per ISO 4217)"""

    discount_percent: Optional[float] = None
    """Actual discount relative value"""

    price_per_hour: Optional[float] = None
    """Price of the item charged per hour"""

    price_per_month: Optional[float] = None
    """Price of the item charged per month"""

    price_status: Literal["error", "hide", "show"]
    """Price status for the UI"""

    price_without_discount_per_month: Optional[float] = None
    """Total price VAT inclusive per month without discount"""

    tax_percent: float
    """Tax rate applied to the subtotal, represented as a percentage"""


class LifecyclePolicyEstimateMaxUsageResponse(BaseModel):
    max_cost: MaxCost
    """Total billed cost of all snapshots that can be created by the schedule.

    Cost of `max_volume_snapshot_count_usage` snapshots.
    """

    max_volume_snapshot_count_usage: int
    """
    Count of snapshots that can be created if the schedule creates the maximum
    possible number of snapshots.
    """

    max_volume_snapshot_sequence_length: int
    """Maximum volume snapshot sequence length."""

    max_volume_snapshot_size_usage: int
    """
    The amount of memory in GiB that snapshots will take up if the schedule creates
    the maximum possible number of them.
    """
