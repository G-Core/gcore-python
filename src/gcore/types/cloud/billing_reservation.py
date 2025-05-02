# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BillingReservation", "AmountPrices", "Resource"]


class AmountPrices(BaseModel):
    commit_price_per_month: str
    """Commit price of the item charged per month"""

    commit_price_per_unit: str
    """Commit price of the item charged per hour"""

    commit_price_total: str
    """Commit price of the item charged for all period reservation"""

    currency_code: str
    """Currency code (3 letter code per ISO 4217)"""

    overcommit_price_per_month: str
    """Overcommit price of the item charged per month"""

    overcommit_price_per_unit: str
    """Overcommit price of the item charged per hour"""

    overcommit_price_total: str
    """Overcommit price of the item charged for all period reservation"""


class Resource(BaseModel):
    activity_period: str
    """Name of the billing period, e.g month"""

    activity_period_length: int
    """Length of the full reservation period by `activity_period`"""

    billing_plan_item_id: int
    """Billing plan item id"""

    commit_price_per_month: str
    """Commit price of the item charged per month"""

    commit_price_per_unit: str
    """Commit price of the item charged per hour"""

    commit_price_total: str
    """Commit price of the item charged for all period reservation"""

    overcommit_billing_plan_item_id: int
    """Overcommit billing plan item id"""

    overcommit_price_per_month: str
    """Overcommit price of the item charged per month"""

    overcommit_price_per_unit: str
    """Overcommit price of the item charged per hour"""

    overcommit_price_total: str
    """Overcommit price of the item charged for all period reservation"""

    resource_count: int
    """Number of reserved resource items"""

    resource_name: str
    """Resource name"""

    resource_type: Literal["flavor"]
    """Resource type"""

    unit_name: str
    """Billing unit name"""

    unit_size_month: str
    """Minimal billing size, for example it is 744 hours per 1 month."""

    unit_size_total: str
    """Unit size month multiplied by count of resources in the reservation"""

    cpu: Optional[str] = None
    """Baremetal CPU description"""

    disk: Optional[str] = None
    """Baremetal disk description"""

    ram: Optional[str] = None
    """Baremetal RAM description"""


class BillingReservation(BaseModel):
    id: int
    """Reservation id"""

    active_from: date
    """Reservation active from date"""

    active_to: date
    """Reservation active to date"""

    activity_period: str
    """Name of the billing period, e.g month"""

    activity_period_length: int
    """Length of the full reservation period by `activity_period`"""

    amount_prices: AmountPrices
    """Reservation amount prices"""

    billing_plan_id: int
    """Billing plan id"""

    created_at: datetime
    """Reservation creation date"""

    error: Optional[str] = None
    """Error message if any occured during reservation"""

    eta: Optional[date] = None
    """ETA delivery if bare metal out of stock.

    Value None means that bare metal in stock.
    """

    is_expiration_message_visible: bool
    """Hide or show expiration message to customer."""

    name: str
    """Reservation name"""

    next_statuses: List[str]
    """List of possible next reservation statuses"""

    region_id: int
    """Region id"""

    region_name: str
    """Region name"""

    remind_expiration_message: Optional[date] = None
    """The date when show expiration date to customer"""

    resources: List[Resource]
    """List of reservation resources"""

    status: str
    """Reservation status"""

    user_status: str
    """User status"""
