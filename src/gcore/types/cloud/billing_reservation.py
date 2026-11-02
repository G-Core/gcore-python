# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["BillingReservation", "ActiveOvercommit", "Commit", "HardwareInfo"]


class ActiveOvercommit(BaseModel):
    """Overcommit pricing details"""

    active_from: datetime
    """Billing subscription active from date"""

    plan_item_id: Optional[int] = None
    """Billing plan item ID"""

    price_per_month: str
    """
    Price per month, per one resource: the price per unit multiplied by
    `unit_size_month`
    """

    price_per_unit: str
    """Price per unit (hourly)"""

    price_total: str
    """Total price for the reservation period for the full reserved amount.

    A reservation with an hourly commit counts the real hours.
    """

    subscription_id: Optional[int] = None
    """Billing subscription ID for overcommit"""


class Commit(BaseModel):
    """Commit pricing details"""

    active_from: datetime
    """Billing subscription active from date"""

    active_to: Optional[datetime] = None
    """Billing subscription active to date"""

    price_per_month: str
    """
    Price per month, per one resource: the price per unit multiplied by
    `unit_size_month`
    """

    price_per_unit: str
    """Price per unit, per one resource (hourly)"""

    price_total: str
    """Total price for the reservation period for the full reserved amount.

    A reservation with an hourly commit counts the real hours.
    """

    subscription_id: Optional[int] = None
    """Billing subscription ID for commit"""


class HardwareInfo(BaseModel):
    """Hardware specifications"""

    cpu: Optional[str] = None
    """CPU specification"""

    disk: Optional[str] = None
    """Disk specification"""

    ram: Optional[str] = None
    """RAM specification"""


class BillingReservation(BaseModel):
    active_billing_plan_id: int
    """Active billing plan ID"""

    active_overcommit: ActiveOvercommit
    """Overcommit pricing details"""

    commit: Commit
    """Commit pricing details"""

    hardware_info: HardwareInfo
    """Hardware specifications"""

    region_name: str
    """Region name"""

    resource_count: int
    """Number of reserved resource items"""

    resource_name: str
    """Resource name"""

    unit_name: str
    """Unit name. Always 'H' (hours)."""

    unit_size_month: str
    """Hours in one month for the monthly prices.

    A reservation with an hourly commit uses the calendar hours of the month of
    `time_from`, limited to the reservation period. Other reservations use 744
    hours.
    """

    unit_size_total: str
    """Total hours of the reservation for all resources.

    A reservation with an hourly commit counts the real hours. Other reservations
    count 744 hours for each month.
    """
