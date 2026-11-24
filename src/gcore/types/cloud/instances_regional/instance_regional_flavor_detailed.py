# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "InstanceRegionalFlavorDetailed",
    "InstanceFlavorExtendedSerializerWithoutPrice",
    "InstanceFlavorExtendedSerializerWithPrice",
]


class InstanceFlavorExtendedSerializerWithoutPrice(BaseModel):
    """Instances flavor schema without price information"""

    architecture: str
    """Flavor architecture type"""

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

    vcpus: int
    """Virtual CPU count"""


class InstanceFlavorExtendedSerializerWithPrice(BaseModel):
    """Instances flavor schema with price information"""

    architecture: str
    """Flavor architecture type"""

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

    vcpus: int
    """Virtual CPU count"""


InstanceRegionalFlavorDetailed: TypeAlias = Union[
    InstanceFlavorExtendedSerializerWithoutPrice, InstanceFlavorExtendedSerializerWithPrice
]
