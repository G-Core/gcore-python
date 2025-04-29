# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .flavor_hardware_description import FlavorHardwareDescription

__all__ = ["LbFlavorList", "Result", "ResultHardwareDescription"]

ResultHardwareDescription: TypeAlias = Union[FlavorHardwareDescription, object]


class Result(BaseModel):
    flavor_id: str
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/flavor_id'
    "$.components.schemas.LbFlavorPricingSerializer.properties.flavor_id"
    """

    flavor_name: str
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/flavor_name'
    "$.components.schemas.LbFlavorPricingSerializer.properties.flavor_name"
    """

    hardware_description: ResultHardwareDescription
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/hardware_description'
    "$.components.schemas.LbFlavorPricingSerializer.properties.hardware_description"
    """

    ram: int
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/ram'
    "$.components.schemas.LbFlavorPricingSerializer.properties.ram"
    """

    vcpus: int
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/vcpus'
    "$.components.schemas.LbFlavorPricingSerializer.properties.vcpus"
    """

    currency_code: Optional[str] = None
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/currency_code/anyOf/0'
    "$.components.schemas.LbFlavorPricingSerializer.properties.currency_code.anyOf[0]"
    """

    price_per_hour: Optional[float] = None
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/price_per_hour/anyOf/0'
    "$.components.schemas.LbFlavorPricingSerializer.properties.price_per_hour.anyOf[0]"
    """

    price_per_month: Optional[float] = None
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/price_per_month/anyOf/0'
    "$.components.schemas.LbFlavorPricingSerializer.properties.price_per_month.anyOf[0]"
    """

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """
    '#/components/schemas/LbFlavorPricingSerializer/properties/price_status/anyOf/0'
    "$.components.schemas.LbFlavorPricingSerializer.properties.price_status.anyOf[0]"
    """


class LbFlavorList(BaseModel):
    count: int
    """
    '#/components/schemas/LbFlavorPricingCollectionSerializer/properties/count'
    "$.components.schemas.LbFlavorPricingCollectionSerializer.properties.count"
    """

    results: List[Result]
    """
    '#/components/schemas/LbFlavorPricingCollectionSerializer/properties/results'
    "$.components.schemas.LbFlavorPricingCollectionSerializer.properties.results"
    """
