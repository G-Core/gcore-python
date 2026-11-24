# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BaremetalRegionalFlavor"]


class BaremetalRegionalFlavor(BaseModel):
    """Bare metal flavor schema"""

    architecture: str
    """Flavor architecture type"""

    capacity: Optional[int] = None
    """Number of available instances of given configuration.

    The value is null if it is not loaded.
    """

    currency_code: Optional[str] = None
    """Currency code. The value is null if the price is not available."""

    disabled: bool
    """Disabled flavor flag"""

    flavor_id: str
    """Flavor ID is the same as name"""

    flavor_name: str
    """Flavor name"""

    hardware_description: Dict[str, str]
    """Additional hardware description"""

    os_type: str
    """Flavor operating system"""

    price_per_hour: Optional[float] = None
    """Price per hour. The value is null if the price is not available."""

    price_per_month: Optional[float] = None
    """Price per month. The value is null if the price is not available."""

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """Price status for the UI. The value is null if the price is not available."""

    ram: int
    """RAM size in MiB"""

    reserved_capacity: Optional[int] = None
    """Number of available instances of given flavor from reservations.

    The value is null if it is not loaded.
    """

    resource_class: Optional[str] = None
    """Flavor resource class for mapping to hardware capacity.

    The value is null if the flavor has no resource class.
    """

    vcpus: int
    """Virtual CPU count. For bare metal flavors, it's a physical CPU count"""
