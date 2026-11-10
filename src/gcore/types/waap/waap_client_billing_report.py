# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .waap_billing_report_item import WaapBillingReportItem

__all__ = ["WaapClientBillingReport"]


class WaapClientBillingReport(BaseModel):
    client_id: int
    """The client ID"""

    items: List[WaapBillingReportItem]
    """The billable consumption items of the client, ordered by date"""
