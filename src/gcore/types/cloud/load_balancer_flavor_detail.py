# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LoadBalancerFlavorDetail"]


class LoadBalancerFlavorDetail(BaseModel):
    flavor_id: str
    """Flavor ID is the same as name"""

    flavor_name: str
    """Flavor name"""

    ram: int
    """RAM size in MiB"""

    vcpus: int
    """Virtual CPU count. For bare metal flavors, it's a physical CPU count"""

    currency_code: Optional[str] = None
    """Currency code. Shown if the `include_prices` query parameter if set to true"""

    price_per_hour: Optional[float] = None
    """Price per hour. Shown if the `include_prices` query parameter if set to true"""

    price_per_month: Optional[float] = None
    """Price per month. Shown if the `include_prices` query parameter if set to true"""

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """Price status for the UI"""
