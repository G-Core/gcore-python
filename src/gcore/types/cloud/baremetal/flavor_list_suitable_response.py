# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["FlavorListSuitableResponse", "Result"]


class Result(BaseModel):
    architecture: str
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/architecture'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.architecture"
    """

    disabled: bool
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/disabled'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.disabled"
    """

    flavor_id: str
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/flavor_id'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.flavor_id"
    """

    flavor_name: str
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/flavor_name'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.flavor_name"
    """

    os_type: str
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/os_type'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.os_type"
    """

    ram: int
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/ram'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.ram"
    """

    resource_class: Optional[str] = None
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/resource_class/anyOf/0'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.resource_class.anyOf[0]"
    """

    vcpus: int
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/vcpus'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.vcpus"
    """

    capacity: Optional[int] = None
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/capacity/anyOf/0'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.capacity.anyOf[0]"
    """

    currency_code: Optional[str] = None
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/currency_code/anyOf/0'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.currency_code.anyOf[0]"
    """

    hardware_description: Optional[Dict[str, str]] = None
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/hardware_description'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.hardware_description"
    """

    price_per_hour: Optional[float] = None
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/price_per_hour/anyOf/0'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.price_per_hour.anyOf[0]"
    """

    price_per_month: Optional[float] = None
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/price_per_month/anyOf/0'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.price_per_month.anyOf[0]"
    """

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/price_status/anyOf/0'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.price_status.anyOf[0]"
    """

    reserved_in_stock: Optional[int] = None
    """
    '#/components/schemas/BareMetalFlavorExtendedSerializer/properties/reserved_in_stock/anyOf/0'
    "$.components.schemas.BareMetalFlavorExtendedSerializer.properties.reserved_in_stock.anyOf[0]"
    """


class FlavorListSuitableResponse(BaseModel):
    count: int
    """
    '#/components/schemas/BareMetalFlavorExtendedCollectionSerializer/properties/count'
    "$.components.schemas.BareMetalFlavorExtendedCollectionSerializer.properties.count"
    """

    results: List[Result]
    """
    '#/components/schemas/BareMetalFlavorExtendedCollectionSerializer/properties/results'
    "$.components.schemas.BareMetalFlavorExtendedCollectionSerializer.properties.results"
    """
