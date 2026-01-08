# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "FlavorListResponse",
    "Result",
    "ResultInstanceFlavorExtendedSerializerWithoutPrice",
    "ResultInstanceFlavorExtendedSerializerWithPrice",
]


class ResultInstanceFlavorExtendedSerializerWithoutPrice(BaseModel):
    """Instances flavor schema without price information"""

    architecture: str
    """Flavor architecture type"""

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

    ram: int
    """RAM size in MiB"""

    vcpus: int
    """Virtual CPU count"""


class ResultInstanceFlavorExtendedSerializerWithPrice(BaseModel):
    """Instances flavor schema with price information"""

    architecture: str
    """Flavor architecture type"""

    currency_code: Optional[str] = None
    """Currency code"""

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
    """Price per hour"""

    price_per_month: Optional[float] = None
    """Price per month"""

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """Price status for the UI"""

    ram: int
    """RAM size in MiB"""

    vcpus: int
    """Virtual CPU count"""


Result: TypeAlias = Union[
    ResultInstanceFlavorExtendedSerializerWithoutPrice, ResultInstanceFlavorExtendedSerializerWithPrice
]


class FlavorListResponse(BaseModel):
    count: int
    """Number of objects"""

    results: List[Result]
    """Objects"""
