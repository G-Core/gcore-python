# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = [
    "GPUBaremetalFlavor",
    "GPUBaremetalFlavorSerializerWithoutPrice",
    "GPUBaremetalFlavorSerializerWithoutPriceHardwareDescription",
    "GPUBaremetalFlavorSerializerWithoutPriceHardwareProperties",
    "GPUBaremetalFlavorSerializerWithoutPriceSupportedFeatures",
    "GPUBaremetalFlavorSerializerWithPrices",
    "GPUBaremetalFlavorSerializerWithPricesHardwareDescription",
    "GPUBaremetalFlavorSerializerWithPricesHardwareProperties",
    "GPUBaremetalFlavorSerializerWithPricesPrice",
    "GPUBaremetalFlavorSerializerWithPricesSupportedFeatures",
]


class GPUBaremetalFlavorSerializerWithoutPriceHardwareDescription(BaseModel):
    """Additional bare metal hardware description"""

    cpu: str
    """Human-readable CPU description"""

    disk: str
    """Human-readable disk description"""

    gpu: str
    """Human-readable GPU description"""

    network: str
    """Human-readable NIC description"""

    ram: str
    """Human-readable RAM description"""


class GPUBaremetalFlavorSerializerWithoutPriceHardwareProperties(BaseModel):
    """Additional bare metal hardware properties"""

    gpu_count: Optional[int] = None
    """The total count of available GPUs."""

    gpu_manufacturer: Optional[str] = None
    """The manufacturer of the graphics processing GPU"""

    gpu_model: Optional[str] = None
    """GPU model"""

    nic_eth: Optional[str] = None
    """The configuration of the Ethernet ports"""

    nic_ib: Optional[str] = None
    """The configuration of the InfiniBand ports"""


class GPUBaremetalFlavorSerializerWithoutPriceSupportedFeatures(BaseModel):
    """Set of enabled features based on the flavor's type and configuration"""

    security_groups: bool


class GPUBaremetalFlavorSerializerWithoutPrice(BaseModel):
    architecture: Optional[str] = None
    """Flavor architecture type"""

    capacity: int
    """Number of available instances of given flavor"""

    disabled: bool
    """If the flavor is disabled, new resources cannot be created using this flavor."""

    hardware_description: GPUBaremetalFlavorSerializerWithoutPriceHardwareDescription
    """Additional bare metal hardware description"""

    hardware_properties: GPUBaremetalFlavorSerializerWithoutPriceHardwareProperties
    """Additional bare metal hardware properties"""

    name: str
    """Flavor name"""

    supported_features: GPUBaremetalFlavorSerializerWithoutPriceSupportedFeatures
    """Set of enabled features based on the flavor's type and configuration"""


class GPUBaremetalFlavorSerializerWithPricesHardwareDescription(BaseModel):
    """Additional virtual hardware description"""

    cpu: str
    """Human-readable CPU description"""

    disk: str
    """Human-readable disk description"""

    gpu: str
    """Human-readable GPU description"""

    network: str
    """Human-readable NIC description"""

    ram: str
    """Human-readable RAM description"""


class GPUBaremetalFlavorSerializerWithPricesHardwareProperties(BaseModel):
    """Additional bare metal hardware properties"""

    gpu_count: Optional[int] = None
    """The total count of available GPUs."""

    gpu_manufacturer: Optional[str] = None
    """The manufacturer of the graphics processing GPU"""

    gpu_model: Optional[str] = None
    """GPU model"""

    nic_eth: Optional[str] = None
    """The configuration of the Ethernet ports"""

    nic_ib: Optional[str] = None
    """The configuration of the InfiniBand ports"""


class GPUBaremetalFlavorSerializerWithPricesPrice(BaseModel):
    """Flavor price"""

    currency_code: Optional[str] = None
    """Currency code. Shown if the `include_prices` query parameter if set to true"""

    price_per_hour: Optional[float] = None
    """Price per hour. Shown if the `include_prices` query parameter if set to true"""

    price_per_month: Optional[float] = None
    """Price per month. Shown if the `include_prices` query parameter if set to true"""

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """Price status for the UI"""


class GPUBaremetalFlavorSerializerWithPricesSupportedFeatures(BaseModel):
    """Set of enabled features based on the flavor's type and configuration"""

    security_groups: bool


class GPUBaremetalFlavorSerializerWithPrices(BaseModel):
    architecture: Optional[str] = None
    """Flavor architecture type"""

    capacity: int
    """Number of available instances of given flavor"""

    disabled: bool
    """If the flavor is disabled, new resources cannot be created using this flavor."""

    hardware_description: GPUBaremetalFlavorSerializerWithPricesHardwareDescription
    """Additional virtual hardware description"""

    hardware_properties: GPUBaremetalFlavorSerializerWithPricesHardwareProperties
    """Additional bare metal hardware properties"""

    name: str
    """Flavor name"""

    price: GPUBaremetalFlavorSerializerWithPricesPrice
    """Flavor price"""

    supported_features: GPUBaremetalFlavorSerializerWithPricesSupportedFeatures
    """Set of enabled features based on the flavor's type and configuration"""


GPUBaremetalFlavor: TypeAlias = Union[GPUBaremetalFlavorSerializerWithoutPrice, GPUBaremetalFlavorSerializerWithPrices]
