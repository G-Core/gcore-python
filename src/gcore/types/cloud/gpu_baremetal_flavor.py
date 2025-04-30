# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "GPUBaremetalFlavor",
    "GPUBaremetalFlavorSerializerWithoutPrice",
    "GPUBaremetalFlavorSerializerWithoutPriceHardwareDescription",
    "GPUBaremetalFlavorSerializerWithoutPriceHardwareProperties",
    "GPUBaremetalFlavorSerializerWithPrices",
    "GPUBaremetalFlavorSerializerWithPricesHardwareDescription",
    "GPUBaremetalFlavorSerializerWithPricesHardwareProperties",
    "GPUBaremetalFlavorSerializerWithPricesPrice",
]


class GPUBaremetalFlavorSerializerWithoutPriceHardwareDescription(BaseModel):
    cpu: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/cpu'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.cpu"
    """

    disk: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/disk'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.disk"
    """

    gpu: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/gpu'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.gpu"
    """

    network: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/network'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.network"
    """

    ram: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/ram'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.ram"
    """


class GPUBaremetalFlavorSerializerWithoutPriceHardwareProperties(BaseModel):
    gpu_count: Optional[int] = None
    """
    '#/components/schemas/GpuFlavorHardwareProperties/properties/gpu_count/anyOf/0'
    "$.components.schemas.GpuFlavorHardwareProperties.properties.gpu_count.anyOf[0]"
    """

    gpu_manufacturer: Optional[str] = None
    """
    '#/components/schemas/GpuFlavorHardwareProperties/properties/gpu_manufacturer/anyOf/0'
    "$.components.schemas.GpuFlavorHardwareProperties.properties.gpu_manufacturer.anyOf[0]"
    """

    gpu_model: Optional[str] = None
    """
    '#/components/schemas/GpuFlavorHardwareProperties/properties/gpu_model/anyOf/0'
    "$.components.schemas.GpuFlavorHardwareProperties.properties.gpu_model.anyOf[0]"
    """


class GPUBaremetalFlavorSerializerWithoutPrice(BaseModel):
    architecture: Optional[str] = None
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithoutPrice/properties/architecture/anyOf/0'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithoutPrice.properties.architecture.anyOf[0]"
    """

    capacity: int
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithoutPrice/properties/capacity'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithoutPrice.properties.capacity"
    """

    disabled: bool
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithoutPrice/properties/disabled'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithoutPrice.properties.disabled"
    """

    hardware_description: GPUBaremetalFlavorSerializerWithoutPriceHardwareDescription
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithoutPrice/properties/hardware_description'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithoutPrice.properties.hardware_description"
    """

    hardware_properties: GPUBaremetalFlavorSerializerWithoutPriceHardwareProperties
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithoutPrice/properties/hardware_properties'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithoutPrice.properties.hardware_properties"
    """

    name: str
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithoutPrice/properties/name'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithoutPrice.properties.name"
    """


class GPUBaremetalFlavorSerializerWithPricesHardwareDescription(BaseModel):
    cpu: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/cpu'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.cpu"
    """

    disk: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/disk'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.disk"
    """

    gpu: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/gpu'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.gpu"
    """

    network: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/network'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.network"
    """

    ram: str
    """
    '#/components/schemas/GpuBaremetalFlavorHardwareDescriptionSerializer/properties/ram'
    "$.components.schemas.GpuBaremetalFlavorHardwareDescriptionSerializer.properties.ram"
    """


class GPUBaremetalFlavorSerializerWithPricesHardwareProperties(BaseModel):
    gpu_count: Optional[int] = None
    """
    '#/components/schemas/GpuFlavorHardwareProperties/properties/gpu_count/anyOf/0'
    "$.components.schemas.GpuFlavorHardwareProperties.properties.gpu_count.anyOf[0]"
    """

    gpu_manufacturer: Optional[str] = None
    """
    '#/components/schemas/GpuFlavorHardwareProperties/properties/gpu_manufacturer/anyOf/0'
    "$.components.schemas.GpuFlavorHardwareProperties.properties.gpu_manufacturer.anyOf[0]"
    """

    gpu_model: Optional[str] = None
    """
    '#/components/schemas/GpuFlavorHardwareProperties/properties/gpu_model/anyOf/0'
    "$.components.schemas.GpuFlavorHardwareProperties.properties.gpu_model.anyOf[0]"
    """


class GPUBaremetalFlavorSerializerWithPricesPrice(BaseModel):
    currency_code: Optional[str] = None
    """
    '#/components/schemas/FlavorPrice/properties/currency_code/anyOf/0'
    "$.components.schemas.FlavorPrice.properties.currency_code.anyOf[0]"
    """

    price_per_hour: Optional[float] = None
    """
    '#/components/schemas/FlavorPrice/properties/price_per_hour/anyOf/0'
    "$.components.schemas.FlavorPrice.properties.price_per_hour.anyOf[0]"
    """

    price_per_month: Optional[float] = None
    """
    '#/components/schemas/FlavorPrice/properties/price_per_month/anyOf/0'
    "$.components.schemas.FlavorPrice.properties.price_per_month.anyOf[0]"
    """

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """
    '#/components/schemas/FlavorPrice/properties/price_status/anyOf/0'
    "$.components.schemas.FlavorPrice.properties.price_status.anyOf[0]"
    """


class GPUBaremetalFlavorSerializerWithPrices(BaseModel):
    architecture: Optional[str] = None
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithPrices/properties/architecture/anyOf/0'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithPrices.properties.architecture.anyOf[0]"
    """

    capacity: int
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithPrices/properties/capacity'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithPrices.properties.capacity"
    """

    disabled: bool
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithPrices/properties/disabled'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithPrices.properties.disabled"
    """

    hardware_description: GPUBaremetalFlavorSerializerWithPricesHardwareDescription
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithPrices/properties/hardware_description'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithPrices.properties.hardware_description"
    """

    hardware_properties: GPUBaremetalFlavorSerializerWithPricesHardwareProperties
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithPrices/properties/hardware_properties'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithPrices.properties.hardware_properties"
    """

    name: str
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithPrices/properties/name'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithPrices.properties.name"
    """

    price: GPUBaremetalFlavorSerializerWithPricesPrice
    """
    '#/components/schemas/GpuBaremetalFlavorSerializerWithPrices/properties/price'
    "$.components.schemas.GpuBaremetalFlavorSerializerWithPrices.properties.price"
    """


GPUBaremetalFlavor: TypeAlias = Union[GPUBaremetalFlavorSerializerWithoutPrice, GPUBaremetalFlavorSerializerWithPrices]
