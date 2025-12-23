# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = [
    "GPUVirtualFlavor",
    "GPUVirtualFlavorSerializerWithoutPrice",
    "GPUVirtualFlavorSerializerWithoutPriceHardwareDescription",
    "GPUVirtualFlavorSerializerWithoutPriceHardwareProperties",
    "GPUVirtualFlavorSerializerWithoutPriceSupportedFeatures",
    "GPUVirtualFlavorSerializerWithPrices",
    "GPUVirtualFlavorSerializerWithPricesHardwareDescription",
    "GPUVirtualFlavorSerializerWithPricesHardwareProperties",
    "GPUVirtualFlavorSerializerWithPricesPrice",
    "GPUVirtualFlavorSerializerWithPricesSupportedFeatures",
]


class GPUVirtualFlavorSerializerWithoutPriceHardwareDescription(BaseModel):
    """Additional virtual hardware description"""

    gpu: Optional[str] = None
    """Human-readable GPU description"""

    local_storage: Optional[int] = None
    """Local storage capacity in GiB"""

    ram: Optional[int] = None
    """RAM size in MiB"""

    vcpus: Optional[int] = None
    """Virtual CPU count"""


class GPUVirtualFlavorSerializerWithoutPriceHardwareProperties(BaseModel):
    """Additional virtual hardware properties"""

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


class GPUVirtualFlavorSerializerWithoutPriceSupportedFeatures(BaseModel):
    """Set of enabled features based on the flavor's type and configuration"""

    security_groups: bool


class GPUVirtualFlavorSerializerWithoutPrice(BaseModel):
    architecture: Optional[str] = None
    """Flavor architecture type"""

    capacity: int
    """Number of available instances of given flavor"""

    disabled: bool
    """If the flavor is disabled, new resources cannot be created using this flavor."""

    hardware_description: GPUVirtualFlavorSerializerWithoutPriceHardwareDescription
    """Additional virtual hardware description"""

    hardware_properties: GPUVirtualFlavorSerializerWithoutPriceHardwareProperties
    """Additional virtual hardware properties"""

    name: str
    """Flavor name"""

    supported_features: GPUVirtualFlavorSerializerWithoutPriceSupportedFeatures
    """Set of enabled features based on the flavor's type and configuration"""


class GPUVirtualFlavorSerializerWithPricesHardwareDescription(BaseModel):
    """Additional virtual hardware description"""

    gpu: Optional[str] = None
    """Human-readable GPU description"""

    local_storage: Optional[int] = None
    """Local storage capacity in GiB"""

    ram: Optional[int] = None
    """RAM size in MiB"""

    vcpus: Optional[int] = None
    """Virtual CPU count"""


class GPUVirtualFlavorSerializerWithPricesHardwareProperties(BaseModel):
    """Additional virtual hardware properties"""

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


class GPUVirtualFlavorSerializerWithPricesPrice(BaseModel):
    """Flavor price."""

    currency_code: Optional[str] = None
    """Currency code. Shown if the `include_prices` query parameter if set to true"""

    price_per_hour: Optional[float] = None
    """Price per hour. Shown if the `include_prices` query parameter if set to true"""

    price_per_month: Optional[float] = None
    """Price per month. Shown if the `include_prices` query parameter if set to true"""

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """Price status for the UI"""


class GPUVirtualFlavorSerializerWithPricesSupportedFeatures(BaseModel):
    """Set of enabled features based on the flavor's type and configuration"""

    security_groups: bool


class GPUVirtualFlavorSerializerWithPrices(BaseModel):
    architecture: Optional[str] = None
    """Flavor architecture type"""

    capacity: int
    """Number of available instances of given flavor"""

    disabled: bool
    """If the flavor is disabled, new resources cannot be created using this flavor."""

    hardware_description: GPUVirtualFlavorSerializerWithPricesHardwareDescription
    """Additional virtual hardware description"""

    hardware_properties: GPUVirtualFlavorSerializerWithPricesHardwareProperties
    """Additional virtual hardware properties"""

    name: str
    """Flavor name"""

    price: GPUVirtualFlavorSerializerWithPricesPrice
    """Flavor price."""

    supported_features: GPUVirtualFlavorSerializerWithPricesSupportedFeatures
    """Set of enabled features based on the flavor's type and configuration"""


GPUVirtualFlavor: TypeAlias = Union[GPUVirtualFlavorSerializerWithoutPrice, GPUVirtualFlavorSerializerWithPrices]
