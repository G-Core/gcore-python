# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WaapBillingReportItem"]


class WaapBillingReportItem(BaseModel):
    amount: int
    """The amount of the billable resource accrued on the date"""

    date: str
    """The date of the accrued billable consumption item"""
