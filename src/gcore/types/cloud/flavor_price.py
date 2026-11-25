# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["FlavorPrice"]


class FlavorPrice(BaseModel):
    currency: str
    """Currency code."""

    discount_percent: float
    """Discount in percent. 0 when there is no discount."""

    flavor_name: str
    """Flavor name."""

    hourly: float
    """Price per hour after the discount."""

    monthly: float
    """Price per month after the discount."""

    monthly_before_discount: float
    """Price per month before the discount."""

    region_id: int
    """Region ID."""
