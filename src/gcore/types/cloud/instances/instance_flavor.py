# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["InstanceFlavor"]


class InstanceFlavor(BaseModel):
    architecture: str
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/architecture'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.architecture"
    """

    disabled: bool
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/disabled'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.disabled"
    """

    flavor_id: str
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/flavor_id'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.flavor_id"
    """

    flavor_name: str
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/flavor_name'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.flavor_name"
    """

    os_type: str
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/os_type'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.os_type"
    """

    ram: int
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/ram'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.ram"
    """

    vcpus: int
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/vcpus'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.vcpus"
    """

    capacity: Optional[int] = None
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/capacity/anyOf/0'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.capacity.anyOf[0]"
    """

    currency_code: Optional[str] = None
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/currency_code/anyOf/0'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.currency_code.anyOf[0]"
    """

    hardware_description: Optional[Dict[str, str]] = None
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/hardware_description'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.hardware_description"
    """

    price_per_hour: Optional[float] = None
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/price_per_hour/anyOf/0'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.price_per_hour.anyOf[0]"
    """

    price_per_month: Optional[float] = None
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/price_per_month/anyOf/0'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.price_per_month.anyOf[0]"
    """

    price_status: Optional[Literal["error", "hide", "show"]] = None
    """
    '#/components/schemas/InstanceFlavorExtendedSerializer/properties/price_status/anyOf/0'
    "$.components.schemas.InstanceFlavorExtendedSerializer.properties.price_status.anyOf[0]"
    """
