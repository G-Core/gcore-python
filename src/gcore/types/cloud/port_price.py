# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PortPrice"]


class PortPrice(BaseModel):
    currency: Optional[str] = None
    """Currency code.

    Null when the port has no IPv4 address on the region's public network. Then all
    prices are 0.
    """

    discount_percent: float
    """Discount in percent. 0 when there is no discount."""

    hourly: float
    """Price per hour after the discount."""

    monthly: float
    """Price per month after the discount."""

    monthly_before_discount: float
    """Price per month before the discount."""

    tax_percent: Optional[float] = None
    """Tax in percent.

    All prices include it. Null when the port has no IPv4 address on the region's
    public network. Then all prices are 0.
    """
