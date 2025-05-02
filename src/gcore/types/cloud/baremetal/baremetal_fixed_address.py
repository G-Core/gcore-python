# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BaremetalFixedAddress"]


class BaremetalFixedAddress(BaseModel):
    addr: str
    """
    '#/components/schemas/BareMetalFixedAddressSerializer/properties/addr'
    "$.components.schemas.BareMetalFixedAddressSerializer.properties.addr"
    """

    interface_name: Optional[str] = None
    """
    '#/components/schemas/BareMetalFixedAddressSerializer/properties/interface_name/anyOf/0'
    "$.components.schemas.BareMetalFixedAddressSerializer.properties.interface_name.anyOf[0]"
    """

    subnet_id: str
    """
    '#/components/schemas/BareMetalFixedAddressSerializer/properties/subnet_id'
    "$.components.schemas.BareMetalFixedAddressSerializer.properties.subnet_id"
    """

    subnet_name: str
    """
    '#/components/schemas/BareMetalFixedAddressSerializer/properties/subnet_name'
    "$.components.schemas.BareMetalFixedAddressSerializer.properties.subnet_name"
    """

    type: Literal["fixed"]
    """
    '#/components/schemas/BareMetalFixedAddressSerializer/properties/type'
    "$.components.schemas.BareMetalFixedAddressSerializer.properties.type"
    """
